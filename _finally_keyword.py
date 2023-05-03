try:
    # Code lines...
    print(ourVariable)
except Exception:
    #optional block
    # Handling of exception (if required)
    print('ourVariable is not defined.')
finally:
    #Code lines... (always executed)
    print('Output is printed successfully.')