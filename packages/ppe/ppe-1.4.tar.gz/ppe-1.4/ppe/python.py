class sum2:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum1(self):
        return self.a +self.b

    def __repr__(self):
    
        """Function to output the characteristics of sum
        
        Args:
            None
        
        Returns:
            string: characteristics of the sum
        
        """
        
        return "a {}, b {}".\
        format(self.a, self.b)