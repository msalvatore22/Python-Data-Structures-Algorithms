def reverse(s):
    if len(s) <= 1:
      return s
    return s[len(s)-1] + reverse(s[0:len(s)-1])

print(reverse("cat"))

strg = "code"
print(strg[len(strg)-1])
print(strg[0:len(strg)-1])