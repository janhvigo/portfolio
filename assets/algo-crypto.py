from typing import Tuple, List, Dict

def read_file(file_path: str) -> any:
    """
    This function reads the dataset containg all the information about the 
    cryptocurrecies. The information are stored in a .txt file.
    
    Parameters:
    :file_path: The current path where the file you want to read is located
    
    @return: A data structure contining the information of the crypto
    """

    # TODO: Implement here your solution
    f = open(file_path, 'r')
    rows = []
    for line in f:
        row = line.split(',')
        row[1] = float(row[1])
        row[2] = float(row[2])
        row[3] = float(row[3])
        rows.append(row)
    return rows

def crypto_stats(data, crypto_name: str, interval: Tuple[int, int]) -> Tuple[float, float, float]:
    """
    This function calculates the minimum, average, and maximum price values of a crypto
    whose name is passed in input within a specific period of time [a,b] passed
    in input. Notice that [a,b] can be an interval that might exceed the actual monitoring
    time of the crypto given in input.
    
    If any error occurs, return the default value (0.0, 0.0, 0.0)
    
    Parameters:
    :data: The data structure used to calculate the statistics
    :crypto_name: The name of the cryptocurrency to calculate statistics for
    :interval: The time interval consisting of a tuple of two values (a,b)
    
    @return: A tuple that contains the minimum, average, and maximum price values
    """
    # TODO: Implement here your solution
    maxx = 0
    minn = 10000
    count = 0
    iterr = 0
    for i in data:
        if i[0] == crypto_name and i[1]>=interval[0] and i[1] <= interval[1]:
            if maxx < i[2]:
                maxx = i[2]
            if minn > i[2]:
                minn = i[2]
            count += i[2]
            iterr += 1
    avg = count / iterr
    return minn, avg, maxx
    


def sort_data(data) -> List[Tuple[str, float]]:
    """
    This function sorts the cryptocurrencies first in alphabetical order, and,
    then, for each of them, it performs a sort according to the day of monitoring.
    
    It is forbidden to use any kind of libraries such as Pandas, or functions like
    list.sort()!
    
    Parameters:
    :data: A data structure containing all the information about the cryptos
    
    @return: A sorted list of tuples containing (crypto name, price)
    """

    # TODO: Implement here your solution
    def QuickSort(arr):
        elements = len(arr)
        if elements < 2:
            return arr
        current_position = 0
        for i in range(1, elements): 
            if arr[i] <= arr[0]:
                current_position += 1
                temp = arr[i]
                arr[i] = arr[current_position]
                arr[current_position] = temp
        temp = arr[0]
        arr[0] = arr[current_position] 
        arr[current_position] = temp 
        left = QuickSort(arr[0:current_position]) 
        right = QuickSort(arr[current_position+1:elements]) 
        arr = left + [arr[current_position]] + right
        return arr
    
    def GetNeededValues(l):
        l = QuickSort(l)
        nl = []
        for el in range(0, len(l)):
            tup = (l[el][0], l[el][2])
            nl.append(tup)
        return nl
    
    res = GetNeededValues(data)
    return res
    


def get_max_value(data, crypto: str, month: int) -> Tuple[int, float]:
    """
    This function must return the maximum price for a given crypto in
    a specific month.
    
    Parameters:
    
    :data: A data structure containing the information about the cryptos.
    :crypto: The crypto for which to search the maximum value.
    :month: The month in which to search for the maximum value.
    
    Assumption: each month contains 30 days. Notice that the month can be
    a natural number in [1,inf). Example the 13th month represents the first
    month of the second year of monitoring; the 14th month represents the
    second month of the second year of monitoring, and so on.
    
    @return: A tuple containing the day in which the crypto reached the maximum price,
             along with the maximum value for that crypto
    """

    # TODO: Implement here your solution
    endperiod = month * 30
    speriod = endperiod - 30
    maxx = -1
    day = -1 
    for i in data:
        if i[0] == crypto and i[1]>=speriod and i[1]<=endperiod:
            if maxx < i[2]:
                maxx = i[2]
                day = i[1]
    return(int(day), float(maxx))


def search(data, value: float, crypto: str) -> Tuple[int, float]:
    """
    This function searches for a specific price in a given data series and
    returns a tuple with the day and the price for a given cryptocurrency.
    If the searched value is not present in the data, the function returns the
    closest price. It compares two values of the data series, one at position i
    and the other at position j, and returns the price closest to the searched value.
    
    N.B.: If you have more than one possible day whose corresponding price is closest
    to the value in input, return the minimum day.
    
    Parameters:
    :data: A data structure that contains the value of price and volume of all cryptos.
    :value: The price value to be searched in the data.
    :crypto: The crypto name to search the value for.
    
    @return: A tuple containing the day on which the cryptocurrency reached the closest price
             and the closest price.
    """

    # TODO: Implement here your solution
    llist = []
    trvalue = 0
    valuefound = False
    for i in data:
        if i[0] == crypto and i[2] == value:
                trvalue = i[2]
                trday = i[1]
                valuefound = True
        elif i[0] == crypto:
                dmin = abs(value - i[2])
                inv = [i[1], i[2], dmin]
                llist.append(inv)
    if valuefound == False:
        minn = llist[0][2]
        d = llist[0][0]
        val = llist[0][1]
        for i in llist:
            if minn > i[2]:
                minn = i[2]
                d = i[0]
                val = i[1]
        return (int(d), val)
    else:
        return (int(trday), trvalue)



def min_correlation_pathways(data,
                             crypto: str,
                             interval: Tuple[int,int]) -> Dict[str, List[str]]:
    """
    This function builds a minimal correlation pathways tree on the given
    data structure for a specific cryptocurrency in a designated temporal
    period. For each node x, the sum of the weights in the path from the root
    to x must be minimal.
    
    Parameters:
    :data: A data structure that contains the information of all cryptos.
    :crypto: The crypto name for which to build the tree.
    :interval: The temporal period for which to build the tree.
               It's in the form [x,y] where x is the beginning time and y is the end
               time.
               
    @return: The minimal correlation pathways tree
    """
    # TODO: Implement here your solution
    
    return None


def correlated_cryptos_at_lvl_k(data,
                                crypto: str,
                                level: int,
                                interval: Tuple[int,int]) -> List[str]:
    """
    This function retrieves the cryptocurrencies related to the one given in input
    at a particular level of correlation in a designated temporal period [x,y].
    
    Parameters:
    :data: A data structure that contains the information of all cryptos.
    :crypto: The crypto name to search correlations for.
    :level: The level at which the correlated cryptos should stand at.
    :interval: The temporal period for which to build the correlation tree.
               It's in the form [x,y] where x is the beginning time and y is the end
               time.
               
    @return: A list of cryptocurrencies
    """
    # TODO: Implement here your solution
    return None