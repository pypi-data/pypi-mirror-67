"""Provide the Query class.
"""

from warnings import warn
import icat.entity
from icat.exception import *

__all__ = ['Query']

substnames = {
    "datafileFormat":"dff",
    "dataset":"ds",
    "dataset.investigation":"i",
    "facility":"f",
    "grouping":"g",
    "instrumentScientists":"isc",
    "investigation":"i",
    "investigationGroups":"ig",
    "investigationInstruments":"ii",
    "investigationUsers":"iu",
    "parameters":"p",
    "parameters.type":"pt",
    "type":"t",
    "user":"u",
    "userGroups":"ug",
}
"""Symbolic names for the representation of related objects in
JOIN ... AS and INCLUDE ... AS.  Prescribing sensible names makes the
search expressions somewhat better readable.  There is no need for
completeness here.
"""

aggregate_fcts = frozenset([
    "DISTINCT",
    "COUNT",
    "COUNT:DISTINCT",
    "MIN",
    "MAX",
    "AVG",
    "AVG:DISTINCT",
    "SUM",
    "SUM:DISTINCT",
])
"""Allowed values for the `function` argument to the
:meth:`icat.query.Query.setAggregate` method.
"""

# ========================== class Query =============================

class Query(object):
    """Build a query to search an ICAT server.

    The query uses the JPQL inspired syntax introduced with ICAT
    4.3.0.  It won't work with older ICAT servers.

    :param client: the ICAT client.
    :type client: :class:`icat.client.Client`
    :param entity: the type of objects to search for.  This may either
        be an :class:`icat.entity.Entity` subclass or the name of an
        entity type.
    :param attribute: the attribute that the query shall return.  See
        the :meth:`~icat.query.Query.setAttribute` method for details.
    :param aggregate: the aggregate function to be applied in the
        SELECT clause, if any.  See the
        :meth:`~icat.query.Query.setAggregate` method for details.
    :param order: the sorting attributes to build the ORDER BY clause
        from.  See the :meth:`~icat.query.Query.setOrder` method for
        details.
    :param conditions: the conditions to build the WHERE clause from.
        See the :meth:`~icat.query.Query.addConditions` method for
        details.
    :param includes: list of related objects to add to the INCLUDE
        clause.  See the :meth:`~icat.query.Query.addIncludes` method
        for details.
    :param limit: a tuple (skip, count) to be used in the LIMIT
        clause.  See the :meth:`~icat.query.Query.setLimit` method for
        details.
    """

    def __init__(self, client, entity, 
                 attribute=None, aggregate=None, order=None, 
                 conditions=None, includes=None, limit=None):
        """Initialize the query.
        """

        super(Query, self).__init__()
        self._init = True
        self.client = client

        if isinstance(entity, basestring):
            self.entity = self.client.getEntityClass(entity)
        elif issubclass(entity, icat.entity.Entity):
            if (entity in self.client.typemap.values() and 
                entity.BeanName is not None):
                self.entity = entity
            else:
                raise EntityTypeError("Invalid entity type '%s'." 
                                      % entity.__name__)
        else:
            raise EntityTypeError("Invalid entity type '%s'." % type(entity))

        self.setAttribute(attribute)
        self.setAggregate(aggregate)
        self.conditions = dict()
        self.addConditions(conditions)
        self.includes = set()
        self.addIncludes(includes)
        self.setOrder(order)
        self.setLimit(limit)
        self._init = None

    def _attrpath(self, attrname):
        """Follow the attribute path along related objects and iterate over
        the components.
        """
        rclass = self.entity
        pattr = ""
        for attr in attrname.split('.'):
            if pattr:
                pattr += ".%s" % attr
            else:
                pattr = attr
            if rclass is None:
                # Last component was not a relation, no further components
                # in the name allowed.
                raise ValueError("Invalid attrname '%s' for %s." 
                                 % (attrname, self.entity.BeanName))
            attrInfo = rclass.getAttrInfo(self.client, attr)
            if attrInfo.relType == "ATTRIBUTE":
                rclass = None
            elif (attrInfo.relType == "ONE" or 
                  attrInfo.relType == "MANY"):
                rclass = self.client.getEntityClass(attrInfo.type)
            else:
                raise InternalError("Invalid relType: '%s'" % attrInfo.relType)
            yield (pattr, attrInfo, rclass)

    def _makesubst(self, objs):
        subst = {}
        substcount = 0
        for obj in sorted(objs):
            i = obj.rfind('.')
            if i < 0:
                continue
            obj = obj[:i]
            for (o, attrInfo, oclass) in self._attrpath(obj):
                if o not in subst:
                    if o in substnames and substnames[o] not in subst.values():
                        subst[o] = substnames[o]
                    else:
                        substcount += 1
                        subst[o] = "s%d" % substcount
        return subst

    def _dosubst(self, obj, subst, addas=True):
        # Note: some old versions of icat.server require the path
        # mentioned in the WHERE clause to contain at least one dot.
        # So the query
        #
        #   SELECT o FROM Rule o JOIN o.grouping AS g WHERE g IS NOT NULL
        #
        # will raise an ICATParameterError with icat.server 4.6.1 and
        # older, while it will work for icat.server 4.7.0 and newer.
        # To remain compatible with the old versions, we always keep
        # one dot after substitution.
        i = obj.rfind('.')
        if i < 0:
            n = "o.%s" % (obj)
        else:
            n = "%s.%s" % (subst[obj[:i]], obj[i+1:])
        if addas and obj in subst:
            n += " AS %s" % (subst[obj])
        return n

    def setAttribute(self, attribute):
        """Set the attribute that the query shall return.

        :param attribute: the name of the attribute.  The result of
            the query will be a list of attribute values for the
            matching entity objects.  If attribute is :const:`None`,
            the result will be the list of matching objects instead.
        :type attribute: :class:`str`
        :raise ValueError: if `attribute` is not valid.
        """
        if attribute is not None:
            # Get the attribute path only to verify that the attribute is valid.
            for (pattr, attrInfo, rclass) in self._attrpath(attribute):
                pass
        self.attribute = attribute

    def setAggregate(self, function):
        """Set the aggregate function to be applied to the result.

        Note that the Query class does not verify whether the
        aggregate function makes any sense for the selected result.
        E.g. the SUM of entity objects or the AVG of strings will
        certainly not work in an ICAT search expression, but it is not
        within the scope of the Query class to reject such nonsense
        beforehand.  Furthermore, "DISTINCT" requires icat.server
        4.7.0 or newer to work.  Again, this is not checked by the
        Query class.

        :param function: the aggregate function to be applied in the
            SELECT clause, if any.  Valid values are "DISTINCT",
            "COUNT", "MIN", "MAX", "AVG", "SUM", or :const:`None`.
            ":DISTINCT", may be appended to "COUNT", "AVG", and "SUM"
            to combine the respective function with "DISTINCT".
        :type function: :class:`str`
        :raise ValueError: if `function` is not a valid.
        """
        if function:
            if function not in aggregate_fcts:
                raise ValueError("Invalid aggregate function '%s'" % function)
            self.aggregate = function
        else:
            self.aggregate = None

    def setOrder(self, order):
        """Set the order to build the ORDER BY clause from.

        :param order: the list of the attributes used for sorting.  A
            special value of :const:`True` may be used to indicate the
            natural order of the entity type.  Any false value means
            no ORDER BY clause.  Rather then only an attribute name,
            any item in the list may also be a tuple of an attribute
            name and an order direction, the latter being either "ASC"
            or "DESC" for ascending or descending order respectively.
        :type order: :class:`list` or :class:`bool`
        :raise ValueError: if `order` contains invalid attributes that
            either do not exist or contain one to many relationships.
        """
        if order is True:

            self.order = [ (a, None) 
                           for a in self.entity.getNaturalOrder(self.client) ]

        elif order:

            self.order = []
            for obj in order:

                if isinstance(obj, tuple):
                    obj, direction = obj
                    if direction not in ("ASC", "DESC"):
                        raise ValueError("Invalid ordering direction '%s'" 
                                         % direction)
                else:
                    direction = None

                for (pattr, attrInfo, rclass) in self._attrpath(obj):
                    if attrInfo.relType == "ONE":
                        if (not attrInfo.notNullable and 
                            pattr not in self.conditions):
                            sl = 3 if self._init else 2
                            warn(QueryNullableOrderWarning(pattr), 
                                 stacklevel=sl)
                    elif attrInfo.relType == "MANY":
                        raise ValueError("Cannot use one to many relationship "
                                         "in '%s' to order %s." 
                                         % (obj, self.entity.BeanName))

                if rclass is None:
                    # obj is an attribute, use it right away.
                    self.order.append( (obj, direction) )
                else:
                    # obj is a related object, use the natural order
                    # of its class.
                    rorder = rclass.getNaturalOrder(self.client)
                    self.order.extend([ ("%s.%s" % (obj, ra), direction) 
                                        for ra in rorder ])

        else:

            self.order = []

    def addConditions(self, conditions):
        """Add conditions to the constraints to build the WHERE clause from.

        :param conditions: the conditions to restrict the search
            result.  This must be a mapping of attribute names to
            conditions on that attribute.  The latter may either be a
            string with a single condition or a list of strings to add
            more then one condition on a single attribute.  If the
            query already has a condition on a given attribute, it
            will be turned into a list with the new condition(s)
            appended.
        :type conditions: :class:`dict`
        :raise ValueError: if any key in `conditions` is not valid.
        """
        if conditions:
            for a in conditions.keys():
                for (pattr, attrInfo, rclass) in self._attrpath(a):
                    pass
                if a in self.conditions:
                    conds = []
                    if isinstance(self.conditions[a], basestring):
                        conds.append(self.conditions[a])
                    else:
                        conds.extend(self.conditions[a])
                    if isinstance(conditions[a], basestring):
                        conds.append(conditions[a])
                    else:
                        conds.extend(conditions[a])
                    self.conditions[a] = conds
                else:
                    self.conditions[a] = conditions[a]

    def addIncludes(self, includes):
        """Add related objects to build the INCLUDE clause from.

        :param includes: list of related objects to add to the INCLUDE
            clause.  A special value of "1" may be used to set (the
            equivalent of) an "INCLUDE 1" clause.
        :type includes: iterable of :class:`str`
        :raise ValueError: if any item in `includes` is not a related object.
        """
        if includes == "1":
            includes = list(self.entity.InstRel)
        if includes:
            for iobj in includes:
                for (pattr, attrInfo, rclass) in self._attrpath(iobj):
                    pass
                if rclass is None:
                    raise ValueError("%s.%s is not a related object." 
                                     % (self.entity.BeanName, iobj))
            self.includes.update(includes)

    def setLimit(self, limit):
        """Set the limits to build the LIMIT clause from.

        :param limit: a tuple (skip, count).
        :type limit: :class:`tuple`
        :raise TypeError: if `limit` is not a tuple of two elements.
        """
        if limit:
            if not(isinstance(limit, tuple) and len(limit) == 2):
                raise TypeError("limit must be a tuple of two elements.")
            self.limit = limit
        else:
            self.limit = None            

    def __repr__(self):
        """Return a formal representation of the query.
        """
        return ("%s(%s, %s, attribute=%s, aggregate=%s, order=%s, "
                "conditions=%s, includes=%s, limit=%s)"
                % (self.__class__.__name__, 
                   repr(self.client), repr(self.entity.BeanName), 
                   repr(self.attribute), repr(self.aggregate), 
                   repr(self.order), repr(self.conditions), 
                   repr(self.includes), repr(self.limit)))

    def __str__(self):
        """Return a string representation of the query.

        Note for Python 2: the result will be an unicode object if any
        of the conditions in the query contains unicode.  This
        violates the specification of the string representation
        operator that requires the return value to be a string object.
        But it is the *right thing* to do to get queries with
        non-ascii characters working.  So this operator favours
        usefulness over formal correctness.  For Python 3, there is no
        distinction between Unicode and string objects anyway.
        """
        joinattrs = { a for a, d in self.order } | set(self.conditions.keys())
        if self.attribute:
            joinattrs.add(self.attribute)
        subst = self._makesubst(joinattrs)
        if self.attribute:
            if self.client.apiversion >= "4.7.0":
                res = self._dosubst(self.attribute, subst, False)
            else:
                # Old versions of icat.server do not accept
                # substitution in the SELECT clause.
                res = "o.%s" % self.attribute
        else:
            res = "o"
        if self.aggregate:
            for fct in reversed(self.aggregate.split(':')):
                res = "%s(%s)" % (fct, res)
        base = "SELECT %s FROM %s o" % (res, self.entity.BeanName)
        joins = ""
        for obj in sorted(subst.keys()):
            joins += " JOIN %s" % self._dosubst(obj, subst)
        if self.conditions:
            conds = []
            for a in sorted(self.conditions.keys()):
                attr = self._dosubst(a, subst, False)
                cond = self.conditions[a]
                if isinstance(cond, basestring):
                    conds.append("%s %s" % (attr, cond))
                else:
                    for c in cond:
                        conds.append("%s %s" % (attr, c))
            where = " WHERE " + " AND ".join(conds)
        else:
            where = ""
        if self.order:
            orders = []
            for a, d in self.order:
                a = self._dosubst(a, subst, False)
                if d:
                    orders.append("%s %s" % (a, d))
                else:
                    orders.append(a)
            order = " ORDER BY " + ", ".join(orders)
        else:
            order = ""
        if self.includes:
            subst = self._makesubst(self.includes)
            includes = set(self.includes)
            includes.update(subst.keys())
            incl = [ self._dosubst(obj, subst) for obj in sorted(includes) ]
            include = " INCLUDE " + ", ".join(incl)
        else:
            include = ""
        if self.limit:
            limit = " LIMIT %s, %s" % self.limit
        else:
            limit = ""
        return base + joins + where + order + include + limit

    def copy(self):
        """Return an independent clone of this query.
        """
        q = Query(self.client, self.entity)
        q.attribute = self.attribute
        q.aggregate = self.aggregate
        q.order = list(self.order)
        q.conditions = self.conditions.copy()
        q.includes = self.includes.copy()
        q.limit = self.limit
        return q
