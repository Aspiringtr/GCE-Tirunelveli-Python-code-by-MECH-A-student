import pandas as pd
print("Mark deails")
d=pd.DataFrame([["English","50/60","55/60","90/100"],
                ["Physics","45/60","40/60","83/100"],
                ["Chemistry","50/60","55/60","90/100"],
                ["Maths","49/60","53/60","95/100"]],
                columns=["subject","Internal1","Internal2","semester"])
print(d)