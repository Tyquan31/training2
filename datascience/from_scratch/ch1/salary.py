from collections import defaultdict

salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
						(40000, 0.7), (76000, 6),
						(69000, 6.5), (76000, 7.5),
						(60000, 2.5), (83000, 10),
						(40000, 1.9), (63000, 4.2)]

""" It seems pretty clear that people with more experience tend to earn more. How can
you turn this into a fun fact? Your first idea is to look at the average salary for each
tenure """

# keys are years, values are lists of the salaries for each tenure
salary_by_tenure = defaultdict(list)
for salary, tenure in salaries_and_tenures:
	salary_by_tenure[tenure].append(salary)
# print(salary_by_tenure)

# keys are years, each value is average salary for that tenure
average_salary_by_tenure = {
	tenure: sum(salaries) / len(salaries)
	for tenure, salaries in salary_by_tenure.items()
}
# print(average_salary_by_tenure)

""" 
This turns out to be not particularly useful, as none of the users have the same tenure,
which means we’re just reporting the individual users’ salaries: 
"""

# It might be more helpful to bucket the tenures
def tenure_bucket(tenure):
	if tenure < 2:
		return "less than two"
	elif tenure < 5:
		return "between two and five"
	else:
		return "more than five"

""" 
Then group together the salaries corresponding to each bucket: 
"""
# keys are tenure buckets, values are lists of salaries for that bucket
salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenures:
	bucket = tenure_bucket(tenure)
	salary_by_tenure_bucket[bucket].append(salary)
# print(salary_by_tenure_bucket)

"""
And finally compute the average salary for each group:
"""
# keys are tenure buckets, values are average salary for that bucket
average_salary_by_bucket = {
	tenure_bucket: sum(salaries) / len(salaries)
	for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}
print("Average salary per bucket\n", average_salary_by_bucket)


""" And you have your soundbite: “Data scientists with more than five years experience
earn 65% more than data scientists with little or no experience!” """

""" 
But we chose the buckets in a pretty arbitrary way. What we’d really like is to make
some sort of statement about the salary effect—on average—of having an additional
year of experience. In addition to making for a snappier fun fact, this allows us to
make predictions about salaries that we don’t know.
"""

















