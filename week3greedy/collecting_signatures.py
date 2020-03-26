def signatures(segments):
    points = []
    segments.sort(key=lambda p:p.start)
    firstsegment = segments[0]
    for i in range(1,len(segments)):
        segmenttocompare = segments[i]
        
        if segmenttocompare.start <= firstsegment.end:
            firstsegment.start = segmenttocompare.start
            if segmenttocompare.end <=
            #firstsegment.end = firstsegment._end
        else:
            points.append(firstsegment.end)
            firstsegment = segmenttocompare
    #if len(points) == 0:
    points.append(firstsegment.end)
        
    return points

def printList(iter):
    for it in iter:
        print(it)



class Segment:
    def __init__(self,start, end):
        self._start = start
        self._end = end
    
    @property
    def start(self):
        return self._start
    
    @start.setter
    def start(self, value):
        self._start = value
    
    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, value):
        self._end = value

    def __str__(self):
        return str(self._start) + ' ' + str(self._end)

    

