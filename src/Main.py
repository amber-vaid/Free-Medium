from Parse import Parse

dir_loc = "Output/"
url = "https://medium.com/better-programming/4-tells-whether-youre-a-great-software-engineer-b0e496ed8f3b?source=extreme_main_feed---------20-73--------------------03fe5134_3aae_4eeb_9e72_415914a36a58--7"
medium = Parse(url)
title, script = medium.generate_webpage()

file = open(dir_loc + title+".html", "w")
file.write(script)
file.close()
print("done")
