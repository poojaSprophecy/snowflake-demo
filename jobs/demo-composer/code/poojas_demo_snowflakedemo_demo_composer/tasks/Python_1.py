def Python_1():

    def abc():
        print("Hello")

    import json
    from datetime import timedelta
    from airflow.operators.python import PythonOperator

    return PythonOperator(task_id = "Python_1", python_callable = abc, show_return_value_in_logs = True)
