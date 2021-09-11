"""

If the same function gets called again and again e.g.
in ML a model reading the input
or some task which needs some sleep

In such case coroutine comes into picture so that the time consuming task
can be avoided and needs not to be performed everytime in the function call

"""


def some_time_consuming_task():
    import time
    text = "some of my text is some and some"
    print("Stating the model reading")
    time.sleep(4)
    print("Model reading completed")

    while True:
        user_input = (yield)

        if user_input in text:
            print("Text is present")
        else:
            print("Text is not present")


task = some_time_consuming_task()
print("Starting the coroutine")
next(task)
print("Ending the coroutine")
task.send("is")
task.send("isi")
print("Closing the coroutine")
task.close()
