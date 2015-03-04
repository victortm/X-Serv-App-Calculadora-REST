#!/usr/bin/python

import webapp

class calcServ(webapp.webApp):

    def parse(self, request):
        verb = request.split(' ')[0]
        resource = request.split(' ')[1]
        body = request.split('\r\n\r\n')[1]
        return(verb, resource, body)

    def process(self,parsedRequest):
        (verb, resource, body) = parsedRequest
        if verb == "PUT":
            self.op = body.split(' ') 
            factor1 = self.op[0] 
            sign = self.op[1]
            factor2 = self.op[2]       
            if len(self.op) != 3:
                httpCode = "400 Bad request"
                htmlBody = "<html><body>Input error</body></html>"
                return (httpCode, htmlBody)
            else:
                if sign == "+":
                    self.sol = float(factor1) + float(factor2)
                elif sign == "-":
                    self.sol = float(factor1) - float(factor2)
                elif sign == "*":
                    self.sol = float(factor1) * float(factor2)
                elif sign == "/":
                    self.sol = float(factor1) / float(factor2)
                httpCode = "200 OK"
                htmlBody = "<html><body>Received arguments: " \
                           + body + "</body></html>"
                return (httpCode, htmlBody)
        elif verb == "GET":
            httpCode = "200 OK"    
            htmlBody = "<html><body>Solution:" \
                       + str(self.sol) + "</body></html>"
            return (httpCode, htmlBody)
  

if __name__ == "__main__":
    serv = calcServ("localhost", 1234)
