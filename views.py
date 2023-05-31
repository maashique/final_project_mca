from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
# Create your views here.
import numpy as np
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer

from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score


dataset = pd.read_csv('D:\\Final Project\\pricePrediction\\Reviews.tsv', delimiter = '\t', quoting = 3)


corpus = []
for i in range(0, 1000):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(('english'))]
    review = ' '.join(review)
    corpus.append(review)

cv = CountVectorizer(max_features = 1500)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)

#MultinomialNB model
print("MultinomialNB")
classifier = MultinomialNB(alpha=0.1)
classifier.fit(X_train, y_train)


def index(request):
    return render(request, "index.html")


def registration(request):
    msg = ''
    if request.POST:
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        address = request.POST["address"]
        file = request.FILES["file"]
        password = request.POST['password']
        cPassword = request.POST['cPassword']
        userLog = User.objects.create_user(username=email, password=password, is_active = 0)
        userLog.save()
        user = Registration.objects.create(
            name=name, email=email, phone=phone, address=address, prof=file, user=userLog)
        user.save()
       
        msg = "Registration successful"
    return render(request, "registration.html", {"msg": msg})

def adminProduct(request):
    msg = ''
    if request.POST:
        name = request.POST["name"]
        phone = request.POST["Desc"]
        address = request.FILES["img"]
      
        user = Products.objects.create(
            name=name,  desc=phone, img=address)
        user.save()
       
        msg = "Registration successful"
    return render(request, "adminProduct.html", {"msg": msg})


def login(request):
    msg = ''
    if request.POST:
        email = request.POST["email"]
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_superuser == 1:
                return redirect("/adminHome")
            elif user.is_active == 1 and user.is_superuser == 0:
                cust = Registration.objects.get(email=email)
                request.session['user'] = cust.id
                return redirect("/userProducts")
                # return redirect("/userHome")
        else:
            msg = "Error Occured"
    return render(request, "login.html", {"msg": msg})


def adminHome(request):

    return render(request, "adminHome.html")

def userApp(request):
    id=request.GET.get("id")
    cust = User.objects.get(id=id)
    cust.is_active = 1
    cust.save()
    return redirect("/adminUsers")

def userRem(request):
    id=request.GET.get("idf")
    cust = User.objects.get(id=id).delete()
    
    
    return redirect("/adminUsers")


def adminFeedback(request):
    fbs = Feedback.objects.all().order_by("-id")
    return render(request, "adminFeedback.html", {"fbs": fbs})

def adminUsers(request):
    fbs = Registration.objects.all().order_by("-id")
    return render(request, "adminUsers.html", {"fbs": fbs})


def userHome(request):
    uid = request.session['user']
    cust = Registration.objects.get(id=uid)
    return render(request, "userHome.html", {"cust": cust})


def favourites(request):
    ms = ""
    if 'msg' in request.GET:
        if request.GET['msg'] == 'Exists':
            ms = "Already Exists"
        else:
            ms = "Added to Wishlist"
    uid = request.session['user']
    datas = Wishlist.objects.filter(user=uid).order_by("-id")
    return render(request, "favourites.html", {"msg": ms, "datas": datas})


def deleteFav(request):
    id = request.GET['id']
    fav = Wishlist.objects.get(id=id)
    fav.delete()
    return redirect("/favourites")


def feedback(request):
    uid = request.session['user']
    cust = Registration.objects.get(id=uid)
    if request.POST:
        feedback = request.POST['feedback']
        feedbacks = Feedback.objects.create(feedback=feedback, user=cust)
        feedbacks.save()
        return redirect("/feedback")

    return render(request, "feedback.html")



def prodReview(request):
    id=request.GET.get('id')
    uid = request.session["user"]
    u = Registration.objects.get(id=uid)
    pid=Products.objects.get(id=id)

    if request.POST:
        rev=request.POST["review"]
        id=request.POST["hotel"]
        hotel=Products.objects.get(id=id)
        new_review = rev
        new_review = re.sub('[^a-zA-Z]', ' ', new_review)
        new_review = new_review.lower()
        new_review = new_review.split()
        ps = PorterStemmer()
        all_stopwords = ["not","is","isnot","isnotnot","a"]
        all_stopwords.remove('not')
        new_review = [ps.stem(word) for word in new_review if not word in set(all_stopwords)]
        new_review = ' '.join(new_review)
        new_corpus = [new_review]
        new_X_test = cv.transform(new_corpus).toarray()
        new_y_pred = classifier.predict(new_X_test)

        rat=hotel.pRev
        
        newRat = int(rat)+int(new_y_pred)
        hotel.pRev = newRat
        hotel.save()
        
        r=Reviews.objects.create(pid=hotel,user=u,review=rev)
        r.save()
            # messages.info(request, 'some error occured')
        hotel2=Products.objects.get(id=id)
        rat1=hotel2.pRev
        total=Reviews.objects.filter(pid__id=id).count()
        print("******TOTAL*********")
        print(total)
        star=float(rat1) / int(total)
        star=round(star,2)
        star=star * 5
        print("******STAR*********")
        print(star)
        hotel2.Rat=round(star,2)
        hotel2.save()


    return  render(request, "prodReview.html",{"pid":pid})


def compareprod(request):
    nme=request.GET.get('name')
    piid=request.GET.get('id')
    pid=Products.objects.get(id=piid)
    pro = ""
    fp = ""
    ap = ""
    fLink = ""
    aLink = ""
    fName = ""
    aName = ""
    r1 = ""
    r2 = ""
    res = ''
    img1 = ''
    img2 = ''
    d1 = ''
    d2 = ''
    d3 = ''
    cRate, cLink, cName, desDu, cImg, r3 = '', '', '', '', '', ''
    uid = request.session['user']
    cust = Registration.objects.get(id=uid)
    if request.POST:
        product = request.POST['product']
        from .comp import main
        pro, fp, ap, fLink, aLink, fName, aName, r1, r2, img1, img2, d1, d2, d3, cRate, cLink, cName, desDu, cImg, r3 = main(
            product)
        print(ap, aName)
        req = Requirements.objects.create(desc=product, user=cust, pid=pid)
        req.save()
    
        if r1 == 'T' and r2 == 'T' and r3 == 'T':
            res = Response.objects.create(
                url1=fLink, desc1=fName, rate1=fp, url2=aLink, desc2=aName, rate2=ap, requirements=req, img1=img1, img2=img2, url3=cLink, desc3=cName, rate3=cRate, img3=cImg)
            res.save()
        elif r1 == 'T' and r2 == 'F' and r3 == 'T':
            res = "No Data"
            res = Response.objects.create(
                url1=fLink, desc1=fName, rate1=fp, url2=res, desc2=res, rate2=res, requirements=req, img1=img1, img2=res, url3=cLink, desc3=cName, rate3=cRate, img3=cImg)
            res.save()
        elif r1 == 'F' and r2 == 'T' and r3 == 'T':
            res = "No Data"
            res = Response.objects.create(
                url1=res, desc1=res, rate1=res, url2=aLink, desc2=aName, rate2=ap, requirements=req, img1=res, img2=img2, url3=cLink, desc3=cName, rate3=cRate, img3=cImg)
            res.save()
        elif r1 == 'F' and r2 == 'F' and r3 == 'T':
            res = "No Data"
            res = Response.objects.create(
                url1=res, desc1=res, rate1=res, url2=res, desc2=res, rate2=res, requirements=req, img1=res, img2=res, url3=cLink, desc3=cName, rate3=cRate, img3=cImg)
            res.save()
        elif r1 == 'T' and r2 == 'T' and r3 == 'F':
            res = "No Data"
            res = Response.objects.create(
                url1=fLink, desc1=fName, rate1=fp, url2=aLink, desc2=aName, rate2=ap, requirements=req, img1=img1, img2=img2, url3=res, desc3=res, rate3=res, img3=res)
            res.save()
        elif r1 == 'T' and r2 == 'F' and r3 == 'F':
            res = "No Data"
            res = Response.objects.create(
                url1=fLink, desc1=fName, rate1=fp, url2=res, desc2=res, rate2=res, requirements=req, img1=img1, img2=res, url3=res, desc3=res, rate3=res, img3=res)
            res.save()
        elif r1 == 'F' and r2 == 'T' and r3 == 'F':
            res = "No Data"
            res = Response.objects.create(
                url1=res, desc1=res, rate1=res, url2=aLink, desc2=aName, rate2=ap, requirements=req, img1=res, img2=img2, url3=res, desc3=res, rate3=res, img3=res)
            res.save()
        else:
            res = Response.objects.create(
                url1=res, desc1=res, rate1=res, url2=res, desc2=res, rate2=res, requirements=req, img1=res, img2=res, url3=res, desc3=res, rate3=res, img3=res)
            res.save()

    return render(request, "compareprod.html", {"pro": pro, "fp": fp, "ap": ap, "fLink": fLink, "aLink": aLink, "fName": fName, "aName": aName, "r1": r1, "r2": r2, "res": res, "img1": img1, "img2": img2, "d1": d1, "d2": d2, "d3": d3, "cName": cName, "cRate": cRate, "cImg": cImg, "cLink": cLink, "r3": r3,"nme":nme})


def history(request):
    uid = request.session['user']
    res = Response.objects.filter(requirements__user=uid).order_by("-id")
    wis = Wishlist.objects.all()
    # favs = Wishlist.objects.filter(user=uid,site='flipkart').only("response")
    # for f in favs:
    #     favList.append(f.response.id)
    # print(favList)
    return render(request, "history.html", {"res": res, "wis": wis})

def userProducts(request):
    uid = request.session['user']
    data=Products.objects.all()
    return render(request, "userProducts.html",{"data": data})


def deleteHistory(request):
    id = request.GET['id']
    res = Response.objects.get(id=id)
    res.delete()
    return redirect("/history")


def addToWish(request):
    res = request.GET['res']
    si = request.GET['si']
    uid = request.session['user']
    if Wishlist.objects.filter(site=si, response__id=res).exists():
        return redirect("/favourites?msg=Exists")
    re = Response.objects.get(id=res)
    cust = Registration.objects.get(id=uid)
    wis = Wishlist.objects.create(site=si, user=cust, response=re)
    wis.save()
    return redirect("/favourites?msg=Added")


def notification(request):

    uid = request.session['user']
    data = Wishlist.objects.filter(user=uid)
    newData = []
    from .notification import flip, ama
    for d in data:
        if d.site == 'flipkart':
            print(d.response.url1)
            rate, res, off = flip(d.response.url1)

            if res:
                d.newRate = rate
                d.offer = off
                d.save()
                newData.append(d)
        else:
            rate, res, off = ama(d.response.url2)
            if res:
                d.newRate = rate
                d.offer = off
                d.save()
                newData.append(d)

    return render(request, "notification.html", {"data": newData})
