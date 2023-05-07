# Create deferrable RandomSensor
# The sensor is set to ‘done’ if a random
# number between 0..1 is lower than a given chance

# psuedo code:
# while chance < random.random():
#     (sleep here)
# (set to done here)

# doc: https://airflow.apache.org/docs/apache-airflow/stable/concepts/deferring.html
# check the triggerer container logs
