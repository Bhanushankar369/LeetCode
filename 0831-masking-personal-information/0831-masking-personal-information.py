class Solution:
    def maskPII(self, s: str) -> str:
        if s[0].isalpha():
            name, domain = s.split("@")
            first, last = name[0], name[-1]

            name = first.lower() + 5*'*' + last.lower()

            dlst = []
            for i in range(len(domain)):
                if domain[i].isalpha():
                    dlst.append(domain[i].lower())
                else:
                    dlst.append(domain[i])
            
            return name + '@' + "".join(dlst)
        
        else:
            nums = ""

            for i in range(len(s)-1, -1, -1):
                if s[i].isalnum():
                    nums += s[i]

            code = len(nums) % 10
            print(nums)
            
            if code == 0:
                return "***-***-" + nums[:4][::-1]
            elif code == 1:
                return "+*-***-***-" + nums[:4][::-1]
            elif code == 2:
                return "+**-***-***-" + nums[:4][::-1]
            else:
                return "+***-***-***-" + nums[:4][::-1]