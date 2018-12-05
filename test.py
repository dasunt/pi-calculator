from bottle import route, run, template, request
from decimal import Decimal,getcontext


@route('/pi')
def index():
    """Home Page"""

    return template("pi",message="Enter Parameters")

@route('/pi', method="POST")
def formhandler():
    """Handle the form submission"""

    plcs = request.forms.get('plcs')
    i = request.forms.get('i')

    getcontext().prec = int(plcs)+1
    
    def plouffBig(n):
        pi = Decimal(0)
        k = 0
        while k < n:
            pi += (Decimal(1)/(16**k))*((Decimal(4)/(8*k+1))-(Decimal(2)/(8*k+4))-(Decimal(1)/(8*k+5))-(Decimal(1)/(8*k+6)))
            k += 1
        return pi


    ans = plouffBig(int(i))

    return template("pi", message=str(ans),plcs=plcs,i=i)

@route('/inbox')
def inbox():
    return '<form>First name:<br><input type="text" name="firstname"><br></form> '

@route('/cal')
def cal():
    #num1 = request.query.num1
    #num2 = request.query.num2
    #num3 = num1+num2
    return "dfgdfg" 

run(host='localhost', port=8080, debug=True)