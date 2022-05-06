class MinMaxArray:
    @staticmethod
    def MinMaxElement(arr:list):
        min = 999999999
        max = -999999999
        for i in range(0, len(arr)):
            if arr[i] > max: max = arr[i]
            if arr[i] < min: min = arr[i]
        return [max, min]