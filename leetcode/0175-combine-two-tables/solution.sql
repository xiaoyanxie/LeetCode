# Write your MySQL query statement below
-- Person: firstName, lastName
-- Address: city, state
-- Person.personId == Address.personId

select a.firstName, a.lastName, b.city, b.state
from Person a
left outer join Address b
on a.personId = b.personId

