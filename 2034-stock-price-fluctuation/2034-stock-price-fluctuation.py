from heapq import heappop, heappush, heapify
class StockPrice:

    def __init__(self):
        self.timestampToPriceMapping = {}
        self.maximumPriceHeap = []
        heapify(self.maximumPriceHeap)
        self.minimumPriceHeap = []
        heapify(self.minimumPriceHeap)
        self.latestTimestamp = 0
        

    def update(self, timestamp: int, price: int) -> None:
        self.timestampToPriceMapping[timestamp] = price
                
        if timestamp > self.latestTimestamp:
            self.latestTimestamp = timestamp
        
        heappush(self.maximumPriceHeap, (-price, timestamp))
        heappush(self.minimumPriceHeap, (price, timestamp))
        
        

    def current(self) -> int:
        return self.timestampToPriceMapping[self.latestTimestamp]
        

    def maximum(self) -> int:
        # if we pop from the heap and that price is equal to the price at the timestamp in the hashmap then that's the answer, but if it is not then just pop it because a price for the same timestamp is there down in the heap
        
        currPrice, timestamp = heappop(self.maximumPriceHeap)
        
        while -currPrice != self.timestampToPriceMapping[timestamp]:
            currPrice, timestamp = heappop(self.maximumPriceHeap)
        
        # once we have the updated price for timestamp, this is our answer, also we'll push it back to the heap since it is the updated timestamp
        
        maximumCurrPrice = -currPrice
        
        heappush(self.maximumPriceHeap, (currPrice, timestamp))
        
        return maximumCurrPrice
        
        
        

    def minimum(self) -> int:
        # similar to maximum
        currPrice, timestamp = heappop(self.minimumPriceHeap)
        
        while currPrice != self.timestampToPriceMapping[timestamp]:
            currPrice, timestamp = heappop(self.minimumPriceHeap)
        
        # once we have the updated price for timestamp, this is our answer, also we'll push it back to the heap since it is the updated timestamp
        
        minCurrPrice = currPrice
        
        heappush(self.minimumPriceHeap, (currPrice, timestamp))
        
        return minCurrPrice
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()