import falcon
import random

class RandomNumber:
    def on_get(self, req, resp):
        """Handles GET requests"""

        if 'min' not in req.params:
            raise falcon.HTTPMissingParam('min')

        if 'max' not in req.params:
            raise falcon.HTTPMissingParam('max')
    
        min_n = req.params['min']
        max_n = req.params['max']

        if min_n.isnumeric() == False:
            raise falcon.HTTPInvalidParam('min must be number', min_n)

        if max_n.isnumeric() == False:
            raise falcon.HTTPInvalidParam('max must be number', max_n)

        min_n = int(min_n)
        max_n = int(max_n)

        if min_n > max_n:
            raise falcon.HTTPInvalidParam('min is bigger than max', (min_n, max_n))
        
        number = random.randint(min_n, max_n)
        result = {'lowerLimit': min_n, 'higherLimit': max_n, 'number': number}
        resp.media = result

api = falcon.API()
api.add_route('/random-number', RandomNumber())
