class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        
        /home//foo//
                   ^
        /.home././//.fs/../foo../.../
                                    ^
        
        /..

        stack:
        name: 

        when seeing a '/':
            1. if name is '.', or empty, ignore
            2. if name is '..', pop the stack
            3. otherwise, push the name on to the stack
            4. clear the name
        """

        path += '/'
        stack = []
        name = ''
        for c in path:
            if c == '/':
                if name == '..':
                    if stack: stack.pop()
                elif name and name != '.':
                    stack.append(name)
                name = ''
            else:
                name += c

        return '/' + '/'.join(stack)
