class Javob(object):
   def rimdan_songa(self, s):

      raqamrim = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
      i = 0
      son = 0
      while i < len(s):
         if i+1<len(s) and s[i:i+2] in raqamrim:
            son+=raqamrim[s[i:i+2]]
            i+=2
         else:
            #print(i)
            son+=raqamrim[s[i]]
            i+=1
      return son
rim = str(input("Songa aylantirmoqchi bo'lgan raqamingizni kiriting: "))
print(Javob().rimdan_songa(rim))
