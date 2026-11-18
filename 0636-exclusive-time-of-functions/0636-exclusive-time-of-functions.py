class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        log = list(map(lambda x: tuple(x.split(":")), logs))
        stack = []
        response = [0] * n
        for entry in log:
            function, action, timestamp = entry
            function = int(function)
            timestamp = int(timestamp)
            if len(stack) == 0:
                stack.append(function)
                lastAction = action
                lastTimestamp = timestamp
            else:

                # if(timestamp==lastTimestamp):
                #     response[stack[-1]]+=1

                # if(stack[-1] != lastFuction):
                #     response[stack[-1]]+=1
                response[stack[-1]] += timestamp - lastTimestamp
                if lastAction == "start" and action == "end":
                    response[stack[-1]] += 1
                if lastAction == "end" and action == "start":
                    response[stack[-1]] -= 1
                if action == "start":
                    # response[stack[-1]]+=timestamp-lastTimestamp
                    lastAction='start'
                    stack.append(function)
                else:
                    # response[stack[-1]]+=timestamp-lastTimestamp
                    
                    lastAction='end'
                    stack.pop()
            lastTimestamp = timestamp

        return response
