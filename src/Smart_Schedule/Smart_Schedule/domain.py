import datetime

import optapy
from optapy import problem_fact, planning_id, planning_entity, planning_variable, \
    planning_solution, planning_entity_collection_property, \
    problem_fact_collection_property, \
    value_range_provider, planning_score
from optapy.types import HardSoftScore
from datetime import time

@problem_fact
class Timeslot:
    id: int
    day_of_week: str
    start_time: datetime.time
    end_time: datetime.time

    def __init__(self, id, day_of_week, start_time, end_time):
        self.id = id
        self.day_of_week = day_of_week
        self.start_time = start_time
        self.end_time = end_time

    @planning_id
    def get_id(self):
        return self.id

    def __str__(self):
        return (
                f"Timeslot("
                f"id={self.id}, "
                f"day_of_week={self.day_of_week}, "
                f"start_time={self.start_time}, "
                f"end_time={self.end_time})"
        )


@planning_entity
class Event:
    name: str
    timeslot: Timeslot
    duration: int


    def __init__(self, name, duration, timeslot=None):
        self.name = name
        self.timeslot = timeslot
        self.duration = duration

    @planning_id
    def get_name(self):
        return self.name

    @planning_variable(duration, ["duration"])
    def get_duration(self):
        return self.duration

    @planning_variable(Timeslot, ["timeslotRange"])
    def get_timeslot(self):
        return self.timeslot

    def set_timeslot(self, new_timeslot):
        self.timeslot = new_timeslot

    def __str__(self):
        return (
            f"Event("
            f"timeslot={self.timeslot}, "
            f"name={self.name}, "
            f"duration={self.duration}"
            f")"
        )


def format_list(a_list):
    return ',\n'.join(map(str, a_list))


@planning_solution
class TimeTable:
    timeslot_list: list[Timeslot]
    event_list: list[Event]
    score: HardSoftScore

    def __init__(self, timeslot_list, event_list, score=None):
        self.timeslot_list = timeslot_list
        self.event_list = event_list
        self.score = score

    @problem_fact_collection_property(Timeslot) 
    @value_range_provider("timeslotRange")
    def get_timeslot_list(self):
        return self.timeslot_list

    @planning_entity_collection_property(Event)
    def get_lesson_list(self):
        return self.event_list

    @planning_score(HardSoftScore)
    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score
    
    def __str__(self):
        return (
            f"TimeTable("
            f"timeslot_list={format_list(self.timeslot_list)},\n"
            f"event_list={format_list(self.event_list)},\n"
            f"score={str(self.score.toString()) if self.score is not None else 'None'}"
            f")"
        )


def generate_problem():
    timeslot_list = [
        Timeslot(1, "MONDAY", time(hour=8, minute=30), time(hour=9, minute=30)),
        Timeslot(2, "MONDAY", time(hour=9, minute=30), time(hour=10, minute=30)),
        Timeslot(3, "MONDAY", time(hour=10, minute=30), time(hour=11, minute=30)),
        Timeslot(4, "MONDAY", time(hour=13, minute=30), time(hour=14, minute=30)),
        Timeslot(5, "MONDAY", time(hour=14, minute=30), time(hour=15, minute=30)),
        Timeslot(6, "TUESDAY", time(hour=8, minute=30), time(hour=9, minute=30)),
        Timeslot(7, "TUESDAY", time(hour=9, minute=30), time(hour=10, minute=30)),
        Timeslot(8, "TUESDAY", time(hour=10, minute=30), time(hour=11, minute=30)),
        Timeslot(9, "TUESDAY", time(hour=13, minute=30), time(hour=14, minute=30)),
        Timeslot(10, "TUESDAY", time(hour=14, minute=30), time(hour=15, minute=30)),
    ]
    event_list = [
        Event(60, "Math"),
        Event(45, "English"),
        Event(60, "Physics"),
        
    ]
    event = event_list[0]
    event.set_timeslot(timeslot_list[0])

    return TimeTable(timeslot_list, event_list)