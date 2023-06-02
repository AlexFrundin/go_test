from dataclasses import dataclass, field
from typing import List


@dataclass
class Department:
    name: str
    courses: List['Course'] = field(default_factory=list)
    professors: List['Professor'] = field(default_factory=list)


@dataclass
class Course:
    name: str
    professor: 'Professor'
    department: Department
    year: int
    stream: str
    students: List['Student'] = field(default_factory=list)


@dataclass
class Professor:
    name: str
    department: Department
    courses: List[Course] = field(default_factory=list)


@dataclass
class Student:
    name: str
    year: int
    specialization: str
    courses: List[Course] = field(default_factory=list)


@dataclass
class University:
    name: str
    departments: List[Department] = field(default_factory=list)
