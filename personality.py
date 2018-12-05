import webbrowser as wb
import pyautogui as pg
import time as t

points = 0

show = pg.prompt("What is your favorite show? ")

if show == "parks and rec":
    pg.alert("That is a really good show!")
    points += 2
    wb.open("https://www.google.com/search?q=lisandro+miguens&rlz=1C1GCEA_enUS752US752&tbm=isch&source=iu&ictx=1&fir=5SeYyFmqAu8nqM%253A%252CBXat3W5tnhVZ0M%252C_&usg=AI4_-kTFhZ8bpGwgPzKGzKbO78uYSGdSpA&sa=X&ved=2ahUKEwiLway15o3eAhUhSN8KHRtoDk8Q9QEwA3oECAYQBg#imgrc=5SeYyFmqAu8nqM:")
elif show == "The office":
    pg.alert("I love dwight!")
    points += 5
    wb.open("https://www.google.com/search?q=lisandro+miguens&rlz=1C1GCEA_enUS752US752&tbm=isch&source=iu&ictx=1&fir=5SeYyFmqAu8nqM%253A%252CBXat3W5tnhVZ0M%252C_&usg=AI4_-kTFhZ8bpGwgPzKGzKbO78uYSGdSpA&sa=X&ved=2ahUKEwiLway15o3eAhUhSN8KHRtoDk8Q9QEwA3oECAYQBg#imgrc=5SeYyFmqAu8nqM:")
elif show == "Modern family":
    pg.alert("I love jay!")
    points += 9
    wb.open("https://www.google.com/search?q=lisandro+miguens&rlz=1C1GCEA_enUS752US752&tbm=isch&source=iu&ictx=1&fir=5SeYyFmqAu8nqM%253A%252CBXat3W5tnhVZ0M%252C_&usg=AI4_-kTFhZ8bpGwgPzKGzKbO78uYSGdSpA&sa=X&ved=2ahUKEwiLway15o3eAhUhSN8KHRtoDk8Q9QEwA3oECAYQBg#imgrc=5SeYyFmqAu8nqM:")
elif show == "Ninjago":
    pg.alert("I love the blue ninja")
    points += 1
    wb.open("https://www.google.com/search?q=baby+lion&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiP48WzsJ_eAhUQZd8KHT11BssQ_AUIDigB&biw=1120&bih=537#imgrc=FK9pC5hhQkSmgM:")
elif show == "deadliest catch":
    pg.alert("thats a very good show")
    points += 200
    wb.open("https://www.google.com/search?q=fruit&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwi3_4rcsZ_eAhVjk-AKHa5QCvkQ_AUIDigB&biw=1120&bih=537#imgrc=m14DCIITm9WAkM:")
elif show == "six":
    pg.alert("thats a very good show")
    points += 200
    wb.open("https://www.google.com/search?q=fruit&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwi3_4rcsZ_eAhVjk-AKHa5QCvkQ_AUIDigB&biw=1120&bih=537#imgrc=m14DCIITm9WAkM:")

else:
    pg.alert("your favorite show is " + str(show))
    points += 20
    wb.open("https://www.google.com/search?q=lisandro+miguens&rlz=1C1GCEA_enUS752US752&tbm=isch&source=iu&ictx=1&fir=5SeYyFmqAu8nqM%253A%252CBXat3W5tnhVZ0M%252C_&usg=AI4_-kTFhZ8bpGwgPzKGzKbO78uYSGdSpA&sa=X&ved=2ahUKEwiLway15o3eAhUhSN8KHRtoDk8Q9QEwA3oECAYQBg#imgrc=5SeYyFmqAu8nqM:")
t.sleep(10)
food = pg.prompt("What is your favorite food? ")

if food == "pizza":
    pg.alert("I love pizza!!")
    points += 27
    wb.open("https://www.youtube.com/watch?v=ZkNMZlkrzaU")
elif food == "ice cream":
    pg.alert("I hate getting a brain freeze")
    points += 45
    wb.open("https://www.google.com/search?q=lisandro+miguens&rlz=1C1GCEA_enUS752US752&tbm=isch&source=iu&ictx=1&fir=5SeYyFmqAu8nqM%253A%252CBXat3W5tnhVZ0M%252C_&usg=AI4_-kTFhZ8bpGwgPzKGzKbO78uYSGdSpA&sa=X&ved=2ahUKEwiLway15o3eAhUhSN8KHRtoDk8Q9QEwA3oECAYQBg#imgrc=5SeYyFmqAu8nqM:")
elif food == "Milk shake":
    pg.alert("I love vanilla milk shakes")
    points += 78
    wb.open("https://www.google.com/search?rlz=1C1GCEA_enUS752US752&biw=1120&bih=537&tbm=isch&sa=1&ei=nljHW5ehFYi1ggfBn4DAAQ&q=baby+piglet&oq=baby+piglet&gs_l=img.3..0l10.25113.29455..30220...0.0..0.56.525.11......0....1..gws-wiz-img.......0i67.BzrTKViX3-U#imgrc=Cr-J7011LLzjmM:")
elif food == "Fries":
    pg.alert("I like fries more than ice cream")
    points += 85
    wb.open("https://www.google.com/search?rlz=1C1GCEA_enUS752US752&biw=1120&bih=537&tbm=isch&sa=1&ei=p1nHW9qrKMPm_QbNmbOoDg&q=patrick+the+star&oq=patrick+the+&gs_l=img.1.0.0l10.21130.25412..28004...0.0..0.61.560.12......0....1..gws-wiz-img.......0i67.FEqLeShoJSU#imgrc=K6XQr3mBSInLAM:")
elif food == "Bacon Cheesburger":
    pg.alert("Bacon is the best")
    points += 99
    wb.open("https://www.google.com/search?q=anaconda+snake&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjgiPyrs5_eAhXBTd8KHSkMDHYQ_AUIDigB&biw=1120&bih=537#imgrc=KnaqyWL9k2ZwJM:")
elif food == "pasta":
    pg.alert("pasta is so good")
    points += 400
    wb.open("https://www.google.com/search?q=good+pasta&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjv5rOetJ_eAhXHmeAKHY4XADEQ_AUIDigB&biw=1120&bih=537#imgrc=ULDdmgHtmmgXrM:")
else:
    pg.alert("Your favorite food is" + food)
    points += 105

t.sleep(20)
animal = pg.prompt("What is your favorite animal? ")
if animal == "cats":
    pg.alert("I have a cat")
    points += 30
    wb.open("https://www.google.com/search?q=cute+baby+poodle&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwipm7SIvvfeAhUkheAKHf3pDJUQ_AUIDigB&biw=1242&bih=597#imgrc=MHYx50IQpIjmCM:")
elif animal == "kudu":
    pg.alert("kudus are very big")
    points += 140
    wb.open("https://www.google.com/search?q=baby+kudu&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjV8ILXvvfeAhXDmOAKHVlVCoIQ_AUIDigB&biw=619&bih=588#imgrc=10XZejbGhNi9IM:")
elif animal == "Thomas Jason":
    pg.alert("very wild animal")
    points += 115
    wb.open("https://www.google.com/search?q=albino+deer&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjI_6n7vvfeAhUPVd8KHbxXB-kQ_AUIDigB&biw=619&bih=588#imgrc=bTJN6yfkqw-tMM:")
elif animal == "Teddy Sandler":
    pg.alert("awsome dog")
    points += 300
    wb.open("https://www.google.com/search?q=albino+lion&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj1nKiev_feAhXBmuAKHeDRB6sQ_AUIDigB&biw=619&bih=588#imgrc=ydQqRaAzR10F_M:")
elif animal == "lion":
    pg.alert("lions are dangerous")
    points += 10000
    wb.open("https://www.google.com/search?q=albino+crocodile&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiDwprSv_feAhUqnOAKHXWgDLgQ_AUIDigB&biw=619&bih=588#imgrc=w90kSXcD0u1DeM:")
elif animal == "crocodile":
    pg.alert("they are very fast")
    points += 5000
    wb.open("https://www.google.com/search?q=the+grinch&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwij46jyv_feAhWwT98KHR4MDDgQ_AUIDygC&biw=619&bih=588&dpr=1.1#imgrc=9djbu5h4klklQM:")
else:
    pg.alert("I love animals")
    points += 2227
t.sleep(20)
car = pg.prompt("What is your favorite car? ")
if car == "lambo":
    pg.alert("I love lambos")
    points += 60
    wb.open("https://www.google.com/search?q=the+grinch&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwij46jyv_feAhWwT98KHR4MDDgQ_AUIDygC&biw=619&bih=588&dpr=1.1#imgdii=3HrMSeiSf2CGwM:&imgrc=9djbu5h4klklQM:")
elif car == "ferrari":
    pg.alert("ferraris are not my thing")
    points += 235
    wb.open("https://www.google.com/search?q=reindeer&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiZ7_vfwPfeAhWxnOAKHZ4BDiMQ_AUIDigB&biw=619&bih=588#imgrc=8DGd5Qtcy4asDM:")
elif car == "ford raptor":
    pg.alert("My favorite car")
    points += 515
    wb.open("https://www.google.com/search?q=lamborghini&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwimp4LrwPfeAhVvc98KHS4eDsMQ_AUIDigB&biw=619&bih=588#imgrc=J-BZle0AFfuHjM:")
elif car == "honda":
    pg.alert("not a fan of hondas")
    points += 72
    wb.open("https://www.google.com/search?rlz=1C1GCEA_enUS752US752&biw=619&bih=588&tbm=isch&sa=1&ei=HcL-W4z2LIyyggf6y6uQCQ&q=porsche&oq=porsche&gs_l=img.3..0i67l8j0j0i67.43736.47593..48618...1.0..0.51.362.8......0....1..gws-wiz-img.....0._dusX3pN35s#imgrc=FsqNtX8h5ykCdM:")
elif car == "land rover":
    pg.alert("This is my second favorite car")
    points += 1000
elif car == "mercedes":
    pg.alert("I like the new mercedes")
    points += 9000
else:
    pg.alert("cars are the best")
    points += 4227
t.sleep(20)
trees = pg.prompt("What is your favorite trees? ")
if trees == "pine trees":
    pg.alert("I like pine trees")
    points += 30
elif trees == "maple trees":
    pg.alert("maple trees are not my thing")
    points += 245
elif trees == "spruce trees":
    pg.alert("My favorite trees")
    points += 555
elif trees == "oak":
    pg.alert("not a fan of oak")
    points += 75
elif trees == "douglas fur trees":
    pg.alert("This is my second favorite kind of trees")
    points += 11000
elif trees == "christmas trees":
    pg.alert("I like the tall christmas trees")
    points += 99000
else:
    pg.alert("trees are the best")
    points += 42227
    
pg.alert(points)
