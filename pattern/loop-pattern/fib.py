def febSeq(n:int) -> list:
    if n==0:
        return [0]
    elif n==1:

        return [0,1]

    else:
        res = [0,1]

        for i in range(2, n+1):
            res.append(res[i-1] + res[i-2])

    return res

# assigning strings to the variables

right_alignment = "RIn publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before final copy is available."
  
# printing out aligned text
print(f"{right_alignment : >30}")


print(febSeq(1))