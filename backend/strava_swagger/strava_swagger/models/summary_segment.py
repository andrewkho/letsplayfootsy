# coding: utf-8

"""
    Strava API v3

    The [Swagger Playground](https://developers.strava.com/playground) is the easiest way to familiarize yourself with the Strava API by submitting HTTP requests and observing the responses before you write any client code. It will show what a response will look like with different endpoints depending on the authorization scope you receive from your athletes. To use the Playground, go to https://www.strava.com/settings/api and change your “Authorization Callback Domain” to developers.strava.com. Please note, we only support Swagger 2.0. There is a known issue where you can only select one scope at a time. For more information, please check the section “client code” at https://developers.strava.com/docs.  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from strava_swagger.models.lat_lng import LatLng  # noqa: F401,E501
from strava_swagger.models.summary_segment_effort import SummarySegmentEffort  # noqa: F401,E501


class SummarySegment(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'name': 'str',
        'activity_type': 'str',
        'distance': 'float',
        'average_grade': 'float',
        'maximum_grade': 'float',
        'elevation_high': 'float',
        'elevation_low': 'float',
        'start_latlng': 'LatLng',
        'end_latlng': 'LatLng',
        'climb_category': 'int',
        'city': 'str',
        'state': 'str',
        'country': 'str',
        'private': 'bool',
        'athlete_pr_effort': 'SummarySegmentEffort'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'activity_type': 'activity_type',
        'distance': 'distance',
        'average_grade': 'average_grade',
        'maximum_grade': 'maximum_grade',
        'elevation_high': 'elevation_high',
        'elevation_low': 'elevation_low',
        'start_latlng': 'start_latlng',
        'end_latlng': 'end_latlng',
        'climb_category': 'climb_category',
        'city': 'city',
        'state': 'state',
        'country': 'country',
        'private': 'private',
        'athlete_pr_effort': 'athlete_pr_effort'
    }

    def __init__(self, id=None, name=None, activity_type=None, distance=None, average_grade=None, maximum_grade=None, elevation_high=None, elevation_low=None, start_latlng=None, end_latlng=None, climb_category=None, city=None, state=None, country=None, private=None, athlete_pr_effort=None):  # noqa: E501
        """SummarySegment - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._activity_type = None
        self._distance = None
        self._average_grade = None
        self._maximum_grade = None
        self._elevation_high = None
        self._elevation_low = None
        self._start_latlng = None
        self._end_latlng = None
        self._climb_category = None
        self._city = None
        self._state = None
        self._country = None
        self._private = None
        self._athlete_pr_effort = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if activity_type is not None:
            self.activity_type = activity_type
        if distance is not None:
            self.distance = distance
        if average_grade is not None:
            self.average_grade = average_grade
        if maximum_grade is not None:
            self.maximum_grade = maximum_grade
        if elevation_high is not None:
            self.elevation_high = elevation_high
        if elevation_low is not None:
            self.elevation_low = elevation_low
        if start_latlng is not None:
            self.start_latlng = start_latlng
        if end_latlng is not None:
            self.end_latlng = end_latlng
        if climb_category is not None:
            self.climb_category = climb_category
        if city is not None:
            self.city = city
        if state is not None:
            self.state = state
        if country is not None:
            self.country = country
        if private is not None:
            self.private = private
        if athlete_pr_effort is not None:
            self.athlete_pr_effort = athlete_pr_effort

    @property
    def id(self):
        """Gets the id of this SummarySegment.  # noqa: E501

        The unique identifier of this segment  # noqa: E501

        :return: The id of this SummarySegment.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SummarySegment.

        The unique identifier of this segment  # noqa: E501

        :param id: The id of this SummarySegment.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this SummarySegment.  # noqa: E501

        The name of this segment  # noqa: E501

        :return: The name of this SummarySegment.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SummarySegment.

        The name of this segment  # noqa: E501

        :param name: The name of this SummarySegment.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def activity_type(self):
        """Gets the activity_type of this SummarySegment.  # noqa: E501


        :return: The activity_type of this SummarySegment.  # noqa: E501
        :rtype: str
        """
        return self._activity_type

    @activity_type.setter
    def activity_type(self, activity_type):
        """Sets the activity_type of this SummarySegment.


        :param activity_type: The activity_type of this SummarySegment.  # noqa: E501
        :type: str
        """
        allowed_values = ["Ride", "Run"]  # noqa: E501
        if activity_type not in allowed_values:
            raise ValueError(
                "Invalid value for `activity_type` ({0}), must be one of {1}"  # noqa: E501
                .format(activity_type, allowed_values)
            )

        self._activity_type = activity_type

    @property
    def distance(self):
        """Gets the distance of this SummarySegment.  # noqa: E501

        The segment's distance, in meters  # noqa: E501

        :return: The distance of this SummarySegment.  # noqa: E501
        :rtype: float
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """Sets the distance of this SummarySegment.

        The segment's distance, in meters  # noqa: E501

        :param distance: The distance of this SummarySegment.  # noqa: E501
        :type: float
        """

        self._distance = distance

    @property
    def average_grade(self):
        """Gets the average_grade of this SummarySegment.  # noqa: E501

        The segment's average grade, in percents  # noqa: E501

        :return: The average_grade of this SummarySegment.  # noqa: E501
        :rtype: float
        """
        return self._average_grade

    @average_grade.setter
    def average_grade(self, average_grade):
        """Sets the average_grade of this SummarySegment.

        The segment's average grade, in percents  # noqa: E501

        :param average_grade: The average_grade of this SummarySegment.  # noqa: E501
        :type: float
        """

        self._average_grade = average_grade

    @property
    def maximum_grade(self):
        """Gets the maximum_grade of this SummarySegment.  # noqa: E501

        The segments's maximum grade, in percents  # noqa: E501

        :return: The maximum_grade of this SummarySegment.  # noqa: E501
        :rtype: float
        """
        return self._maximum_grade

    @maximum_grade.setter
    def maximum_grade(self, maximum_grade):
        """Sets the maximum_grade of this SummarySegment.

        The segments's maximum grade, in percents  # noqa: E501

        :param maximum_grade: The maximum_grade of this SummarySegment.  # noqa: E501
        :type: float
        """

        self._maximum_grade = maximum_grade

    @property
    def elevation_high(self):
        """Gets the elevation_high of this SummarySegment.  # noqa: E501

        The segments's highest elevation, in meters  # noqa: E501

        :return: The elevation_high of this SummarySegment.  # noqa: E501
        :rtype: float
        """
        return self._elevation_high

    @elevation_high.setter
    def elevation_high(self, elevation_high):
        """Sets the elevation_high of this SummarySegment.

        The segments's highest elevation, in meters  # noqa: E501

        :param elevation_high: The elevation_high of this SummarySegment.  # noqa: E501
        :type: float
        """

        self._elevation_high = elevation_high

    @property
    def elevation_low(self):
        """Gets the elevation_low of this SummarySegment.  # noqa: E501

        The segments's lowest elevation, in meters  # noqa: E501

        :return: The elevation_low of this SummarySegment.  # noqa: E501
        :rtype: float
        """
        return self._elevation_low

    @elevation_low.setter
    def elevation_low(self, elevation_low):
        """Sets the elevation_low of this SummarySegment.

        The segments's lowest elevation, in meters  # noqa: E501

        :param elevation_low: The elevation_low of this SummarySegment.  # noqa: E501
        :type: float
        """

        self._elevation_low = elevation_low

    @property
    def start_latlng(self):
        """Gets the start_latlng of this SummarySegment.  # noqa: E501


        :return: The start_latlng of this SummarySegment.  # noqa: E501
        :rtype: LatLng
        """
        return self._start_latlng

    @start_latlng.setter
    def start_latlng(self, start_latlng):
        """Sets the start_latlng of this SummarySegment.


        :param start_latlng: The start_latlng of this SummarySegment.  # noqa: E501
        :type: LatLng
        """

        self._start_latlng = start_latlng

    @property
    def end_latlng(self):
        """Gets the end_latlng of this SummarySegment.  # noqa: E501


        :return: The end_latlng of this SummarySegment.  # noqa: E501
        :rtype: LatLng
        """
        return self._end_latlng

    @end_latlng.setter
    def end_latlng(self, end_latlng):
        """Sets the end_latlng of this SummarySegment.


        :param end_latlng: The end_latlng of this SummarySegment.  # noqa: E501
        :type: LatLng
        """

        self._end_latlng = end_latlng

    @property
    def climb_category(self):
        """Gets the climb_category of this SummarySegment.  # noqa: E501

        The category of the climb [0, 5]. Higher is harder ie. 5 is Hors catégorie, 0 is uncategorized in climb_category.  # noqa: E501

        :return: The climb_category of this SummarySegment.  # noqa: E501
        :rtype: int
        """
        return self._climb_category

    @climb_category.setter
    def climb_category(self, climb_category):
        """Sets the climb_category of this SummarySegment.

        The category of the climb [0, 5]. Higher is harder ie. 5 is Hors catégorie, 0 is uncategorized in climb_category.  # noqa: E501

        :param climb_category: The climb_category of this SummarySegment.  # noqa: E501
        :type: int
        """

        self._climb_category = climb_category

    @property
    def city(self):
        """Gets the city of this SummarySegment.  # noqa: E501

        The segments's city.  # noqa: E501

        :return: The city of this SummarySegment.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this SummarySegment.

        The segments's city.  # noqa: E501

        :param city: The city of this SummarySegment.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def state(self):
        """Gets the state of this SummarySegment.  # noqa: E501

        The segments's state or geographical region.  # noqa: E501

        :return: The state of this SummarySegment.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SummarySegment.

        The segments's state or geographical region.  # noqa: E501

        :param state: The state of this SummarySegment.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def country(self):
        """Gets the country of this SummarySegment.  # noqa: E501

        The segment's country.  # noqa: E501

        :return: The country of this SummarySegment.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this SummarySegment.

        The segment's country.  # noqa: E501

        :param country: The country of this SummarySegment.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def private(self):
        """Gets the private of this SummarySegment.  # noqa: E501

        Whether this segment is private.  # noqa: E501

        :return: The private of this SummarySegment.  # noqa: E501
        :rtype: bool
        """
        return self._private

    @private.setter
    def private(self, private):
        """Sets the private of this SummarySegment.

        Whether this segment is private.  # noqa: E501

        :param private: The private of this SummarySegment.  # noqa: E501
        :type: bool
        """

        self._private = private

    @property
    def athlete_pr_effort(self):
        """Gets the athlete_pr_effort of this SummarySegment.  # noqa: E501


        :return: The athlete_pr_effort of this SummarySegment.  # noqa: E501
        :rtype: SummarySegmentEffort
        """
        return self._athlete_pr_effort

    @athlete_pr_effort.setter
    def athlete_pr_effort(self, athlete_pr_effort):
        """Sets the athlete_pr_effort of this SummarySegment.


        :param athlete_pr_effort: The athlete_pr_effort of this SummarySegment.  # noqa: E501
        :type: SummarySegmentEffort
        """

        self._athlete_pr_effort = athlete_pr_effort

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(SummarySegment, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SummarySegment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
