def finalInstances(instances, averageUtil):
    final_instance = instances
    time = 0
    while time < len(averageUtil):
        increment = 1
        if averageUtil[time] < 25:
            updated_instance = final_instance // 2
            if updated_instance > 0:
                final_instance = updated_instance
                increment = 10
        elif averageUtil[time] > 60:
            updated_instance = final_instance * 2
            if updated_instance <= 2 * (pow(10,8)):
                final_instance = updated_instance
                increment = 10
        time += increment

    return final_instance
        

if __name__ == "__main__":
    instances = 2
    # averageUtil = [25, 23, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 76, 80]
    # averageUtil = [25]
    # averageUtil = []
    # averageUtil = [26]
    # averageUtil = [5]
    averageUtil = [90]
    print(finalInstances(instances, averageUtil))