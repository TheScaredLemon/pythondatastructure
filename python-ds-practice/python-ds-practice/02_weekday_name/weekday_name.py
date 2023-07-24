def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
        
    """
    
    
    def weekday_name(day_of_week):
        if (day_of_week) == 1:
            print("Sunday")
        elif day_of_week == 7:
            print("Saturday")
        else:
            print("None")