# %load plane.py
from decimal import Decimal, getcontext

from .vector import Vector

getcontext().prec = 30


class Hyperplane(object):

    NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'
    EITHER_DIM_OR_NORMAL_VEC_MUST_BE_PROVIDED_MSG = 'Either the dimension the hyperplane myst be provided'

    def __init__(self, dimension=None, normal_vector=None, constant_term=None):
        if not dimension and not normal_vector:
            raise Exception(self.EITHER_DIM_OR_NORMAL_VEC_MUST_BE_PROVIDED_MSG)
        elif not normal_vector:
            self.dimension = dimension
            all_zeros = ['0']*self.dimension
            normal_vector = Vector(all_zeros)
        else:
            self.dimension = normal_vector.dimension
        self.normal_vector = normal_vector

        if not constant_term:
            constant_term = Decimal('0')
        self.constant_term = Decimal(constant_term)

        self.set_basepoint()


    def set_basepoint(self):
        try:
            n = self.normal_vector.coordinates
            c = self.constant_term
            basepoint_coords = ['0']*self.dimension

            initial_index = Hyperplane.first_nonzero_index(n)
            initial_coefficient = n[initial_index]

            basepoint_coords[initial_index] = c/initial_coefficient
            self.basepoint = Vector(basepoint_coords)

        except Exception as e:
            if str(e) == Hyperplane.NO_NONZERO_ELTS_FOUND_MSG:
                self.basepoint = None
            else:
                raise e


    def __str__(self):

        num_decimal_places = 3

        def write_coefficient(coefficient, is_initial_term=False):
            coefficient = round(coefficient, num_decimal_places)
            if coefficient % 1 == 0:
                coefficient = int(coefficient)

            output = ''

            if coefficient < 0:
                output += '-'
            if coefficient > 0 and not is_initial_term:
                output += '+'

            if not is_initial_term:
                output += ' '

            if abs(coefficient) != 1:
                output += '{}'.format(abs(coefficient))

            return output

        n = self.normal_vector.coordinates

        try:
            initial_index = Hyperplane.first_nonzero_index(n)
            terms = [write_coefficient(n[i], is_initial_term=(i==initial_index)) + 'x_{}'.format(i+1)
                     for i in range(self.dimension) if round(n[i], num_decimal_places) != 0]
            output = ' '.join(terms)

        except Exception as e:
            if str(e) == self.NO_NONZERO_ELTS_FOUND_MSG:
                output = '0'
            else:
                raise e

        constant = round(self.constant_term, num_decimal_places)
        if constant % 1 == 0:
            constant = int(constant)
        output += ' = {}'.format(constant)

        return output

    def __eq__(self, pln):
        if self.normal_vector.is_zero():
            if not pln.normal_vector.is_zero():
                return False
            else:
                diff = self.constant_term - pln.constant_term
                return MyDecimal(diff).is_near_zero()
        elif pln.normal_vector.is_zero():
            return False
        
        self_bp = self.basepoint
        pln_bp = pln.basepoint
        bp_diff = self_bp - pln_bp
        
        self_nv = self.normal_vector
        return self.is_para(pln) and bp_diff.is_orthog(self_nv)
    
    def __add__(self, pln):
        nv = self.normal_vector + pln.normal_vector
        k = self.constant_term + pln.constant_term
        return Hyperplane(nv.dimension, nv,k)
    
    def __mul__(self, coefficient):
        nv = self.normal_vector * coefficient
        k = self.constant_term * coefficient
        return Hyperplane(nv.dimension, nv,k)

    def __iadd__(self, pln):
        nv = self.normal_vector + pln.normal_vector
        k = self.constant_term + pln.constant_term
        return Hyperplane(nv.dimension, nv,k)
    
    def __imul__(self, coefficient):
        nv = self.normal_vector * coefficient
        k = self.constant_term * coefficient
        return Hyperplane(nv.dimension, nv,k)

    def __rmul__(self, coefficient):
        return self * coefficient
 
    def is_para(self, pln):
        self_nv = self.normal_vector
        pln_nv = pln.normal_vector
        return self_nv.is_para(pln_nv)

    @staticmethod
    def first_nonzero_index(iterable):
        for k, item in enumerate(iterable):
            if not MyDecimal(item).is_near_zero():
                return k
        raise Exception(Hyperplane.NO_NONZERO_ELTS_FOUND_MSG)


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps
