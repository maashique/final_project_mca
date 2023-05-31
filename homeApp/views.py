from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
import pymysql
from django.core.files.storage import FileSystemStorage
import json
from datetime import date
from datetime import datetime
# Create your views here.
db = pymysql.connect(host="localhost", user="root",
                     password="", database="onlineshop")
c = db.cursor()


def home(request):
    return render(request, "index.html")


def customerreg(request):
    if request.method == "POST":
        fName = request.POST['fName']
        lName = request.POST['lName']
        house = request.POST['house']
        street = request.POST['street']
        district = request.POST['district']
        pin = request.POST['pin']
        contact = request.POST['contact']
        email = request.POST['email']
        password = request.POST['password']
        qryCheck = f"SELECT count(*) FROM `login`l, `customers`c, `staffs`s, `vendor`v WHERE l.`username`='{email}' OR c.`contact`='{contact}' OR s.`contact`='{contact}' OR v.`contact`='{contact}'"
        print(qryCheck)
        c.execute(qryCheck)
        check = c.fetchone()
        check = check[0]
        print(check)
        if check > 0:
            msg = "Details already registred.."
            return render(request, "customerReg.html", {"msg": msg})
        else:
            qry = f"INSERT INTO `customers` (`fname`,`lname`,`house`,`street`,`district`,`pincode`,`contact`,`email`) VALUES ('{fName}','{lName}','{house}','{street}','{district}','{pin}','{contact}','{email}')"
            qryLog = f"INSERT INTO `login` (`username`,`password`,`usertype`,`status`) VALUES ('{email}','{password}','customer','1')"
            qrySec = f"INSERT INTO `regsession`(`uid`,`utype`,`date`) VALUES ((SELECT MAX(`cid`) FROM `customers`),'customer', (SELECT SYSDATE()))"
            try:
                c.execute(qry)
                db.commit()
                c.execute(qryLog)
                db.commit()
                c.execute(qrySec)
                db.commit()
                return redirect("login")
            except:
                msg = "Error Occured..."
                return render(request, "customerReg.html", {"msg": msg})
    else:
        return render(request, "customerReg.html")


def customerprofile(request):
    id = request.session['id']
    if request.method == "POST":
        fName = request.POST['fName']
        lName = request.POST['lName']
        house = request.POST['house']
        street = request.POST['street']
        district = request.POST['district']
        pin = request.POST['pin']
        contact = request.POST['contact']
        email = request.POST['email']
        password = request.POST['password']
        qry = f"UPDATE `customers` SET  `fname`='{fName}',`lname`='{lName}',`house`='{house}',`street`='{street}',`district`='{district}',`pincode`='{pin}',`contact`='{contact}' WHERE `cid`='{id}'"
        qryLog = f"UPDATE `login` SET `password`='{password}' WHERE `username`='{email}'"
        try:
            c.execute(qry)
            db.commit()
            c.execute(qryLog)
            db.commit()
            return redirect("customerprofile")
        except:
            msg = "Error Occured..."
            return render(request, "customerprofile.html", {"msg": msg})
    else:
        qryProfile = f"SELECT * FROM `customers`c, `login`l WHERE c.`cid`='{id}' AND c.`email`=l.`username`"
        c.execute(qryProfile)
        data = c.fetchone()
        return render(request, "customerprofile.html", {"data": data})


def vendorreg(request):
    if request.method == "POST":
        fName = request.POST['fName']
        lName = request.POST['lName']
        sName = request.POST['sName']
        street = request.POST['street']
        district = request.POST['district']
        pin = request.POST['pin']
        contact = request.POST['contact']
        email = request.POST['email']
        qryCheck = f"SELECT count(*) FROM `login`l, `customers`c, `staffs`s, `vendor`v WHERE l.`username`='{email}' OR c.`contact`='{contact}' OR s.`contact`='{contact}' OR v.`contact`='{contact}'"
        print(qryCheck)
        c.execute(qryCheck)
        check = c.fetchone()
        check = check[0]
        print(check)
        if check > 0:
            msg = "Details already registred.."
            return render(request, "vendorReg.html", {"msg": msg})
        else:
            qry = f"INSERT INTO `vendor` (`fName`,`lName`,`sName`,`street`,`district`,`pincode`,`contact`,`email`) VALUES ('{fName}','{lName}','{sName}','{street}','{district}','{pin}','{contact}','{email}')"
            try:
                c.execute(qry)
                db.commit()
                return redirect("vendorreg")
            except:
                msg = "Error Occured..."
                return render(request, "vendorReg.html", {"msg": msg})
    else:
        return render(request, "vendorReg.html")


def adminupdatevendor(request):
    if request.method == "POST":
        vid = request.POST['vid']
        fName = request.POST['fName']
        lName = request.POST['lName']
        sName = request.POST['sName']
        street = request.POST['street']
        district = request.POST['district']
        pin = request.POST['pin']
        contact = request.POST['contact']
        email = request.POST['email']
        qry = f"UPDATE `vendor` SET `fName`='{fName}',`lName`='{lName}',`sName`='{sName}',`street`='{street}',`district`='{district}',`pincode`='{pin}',`contact`='{contact}',`email`='{email}' WHERE `vid`={vid}"
        try:
            c.execute(qry)
            db.commit()
            return redirect("/adminviewvendors")
        except:
            msg = "Error Occured..."
            return render(request, "adminupdatevendor.html", {"msg": msg})
    else:
        id = request.GET['id']
        qryVen = f"SELECT * FROM `vendor` WHERE `vid`='{id}'"
        c.execute(qryVen)
        data = c.fetchone()
        return render(request, "adminupdatevendor.html", {"data": data})


def staffreg(request):
    if request.method == "POST":
        fName = request.POST['fName']
        lName = request.POST['lName']
        house = request.POST['house']
        street = request.POST['street']
        district = request.POST['district']
        pin = request.POST['pin']
        contact = request.POST['contact']
        email = request.POST['email']
        password = request.POST['password']
        qryCheck = f"SELECT count(*) FROM `login`l, `customers`c, `staffs`s, `vendor`v WHERE l.`username`='{email}' OR c.`contact`='{contact}' OR s.`contact`='{contact}' OR v.`contact`='{contact}'"
        print(qryCheck)
        c.execute(qryCheck)
        check = c.fetchone()
        check = check[0]
        print(check)
        if check > 0:
            msg = "Details already registred.."
            return render(request, "staffReg.html", {"msg": msg})
        else:
            qry = f"INSERT INTO `staffs` (`fname`,`lname`,`house`,`street`,`district`,`pincode`,`contact`,`email`) VALUES ('{fName}','{lName}','{house}','{street}','{district}','{pin}','{contact}','{email}')"
            qryLog = f"INSERT INTO `login` (`username`,`password`,`usertype`,`status`) VALUES ('{email}','{password}','staff','1')"
            qrySec = f"INSERT INTO `regsession`(`uid`,`utype`,`date`) VALUES ((SELECT MAX(`sid`) FROM `staffs`),'staff', (SELECT SYSDATE()))"
            try:
                c.execute(qry)
                db.commit()
                c.execute(qryLog)
                db.commit()
                c.execute(qrySec)
                db.commit()
                return redirect("staffreg")
            except:
                msg = "Error Occured..."
                return render(request, "staffReg.html", {"msg": msg})
    else:
        return render(request, "staffReg.html")


def login(request):
    if request.method == "POST":
        email = request.POST['uName']
        password = request.POST['password']
        s = f"select count(*) from login where username='{email}'"
        c.execute(s)
        i = c.fetchone()
        if(i[0] > 0):
            s = f"select * from login where username='{email}'"
            print(s)
            c.execute(s)
            i = c.fetchone()
            if(i[2] == password):
                request.session['email'] = email
                if(i[4] == "1"):
                    if(i[3] == "admin"):
                        return redirect("/adminHome")
                    elif(i[3] == "staff"):
                        s = f"select * from staffs where email='{email}'"
                        c.execute(s)
                        d = c.fetchone()
                        request.session['id'] = d[0]
                        return redirect("/staffHome")
                    elif(i[3] == "customer"):
                        s = f"select * from customers where email='{email}'"
                        c.execute(s)
                        d = c.fetchone()
                        request.session['id'] = d[0]
                        return redirect("/customerhome")
                else:
                    msg = "Account is not Active..."
                    return render(request, "login.html", {"msg": msg})
            else:
                msg = "Password Dosen't Match..."
                return render(request, "login.html", {"msg": msg})
        else:
            msg = "Invalid Details..."
            return render(request, "login.html", {"msg": msg})
    else:
        return render(request, "login.html")


def adminHome(request):
    return render(request, "adminHome.html")


def admincategory(request):
    msg = ""
    if request.method == "POST":
        name = request.POST['txtCategory']
        qry = f"SELECT COUNT(*) FROM `category` WHERE `category`='{name}'"
        c.execute(qry)
        count = c.fetchone()
        count = count[0]
        if count > 0:
            msg = "Category already added"
        else:
            s = "insert into category (category) values('"+name+"')"
            print(s)
            try:
                c.execute(s)
                db.commit()
            except:
                msg = "Sorry some error occured"
            else:
                msg = "Category added"
    s = "select * from category"
    c.execute(s)
    data = c.fetchall()
    return render(request, "admincategory.html", {"msg": msg, "data": data})


def updatecategory(request):
    msg = ""
    cid = request.GET.get("id")
    if(request.POST):
        name = request.POST['txtCategory']
        s = "update category set category='"+name+"' where catid='"+cid+"'"
        try:
            c.execute(s)
            db.commit()
        except:
            msg = "Sorry some error occured"
        else:
            msg = "Category updated"
    s = "select * from category where catid='"+cid+"'"
    c.execute(s)
    category = c.fetchall()
    s = "select * from category"
    c.execute(s)
    data = c.fetchall()
    return render(request, "adminupdatecategory.html", {"msg": msg, "data": data, "category": category})


def deletecategory(request):
    msg = ""
    cid = request.GET.get("id")
    status = request.GET['status']
    s = f"UPDATE category SET `status`='{status}' where catid='"+cid+"'"
    c.execute(s)
    db.commit()
    return HttpResponseRedirect("/admincategory")


def adminsubcategory(request):
    msg = ""
    s = "select * from category"
    c.execute(s)
    category = c.fetchall()
    if(request.POST):
        catid = request.POST['cat']
        name = request.POST['txtSubcategory']
        qry = f"SELECT COUNT(*) FROM `subcategory` WHERE `subcategory`='{name}' and `catid`='{catid}'"
        c.execute(qry)
        count = c.fetchone()
        count = count[0]
        if count > 0:
            msg = "Sucategory already added"
        else:
            s = "insert into subcategory (catid,subcategory) values('" + \
                catid+"','"+name+"')"
            try:
                c.execute(s)
                db.commit()
            except:
                msg = "Sorry some error occured"
            else:
                msg = "Subcategory added"
    s = "select subcategory.*,category.category from category,subcategory where category.catid=subcategory.catid"
    c.execute(s)
    data = c.fetchall()
    return render(request, "adminsubcategory.html", {"msg": msg, "data": data, "category": category})


def updatesubcategory(request):
    msg = ""
    cid = request.GET.get("id")
    if(request.POST):
        name = request.POST['txtSubcategory']
        s = "update subcategory set subcategory='"+name+"' where subid='"+cid+"'"
        try:
            c.execute(s)
            db.commit()
        except:
            msg = "Sorry some error occured"
        else:
            msg = "Subcategory updated"
    s = "select subcategory.*,category.category from category,subcategory where category.catid=subcategory.catid and subid='"+cid+"'"
    c.execute(s)
    category = c.fetchall()
    s = "select subcategory.*,category.category from category,subcategory where category.catid=subcategory.catid"
    c.execute(s)
    data = c.fetchall()
    return render(request, "adminupdatesubcategory.html", {"msg": msg, "data": data, "category": category})


def deletesubcategory(request):
    msg = ""
    cid = request.GET.get("id")
    status = request.GET['status']
    s = f"UPDATE subcategory SET `status`='{status}' where subid='"+cid+"'"
    print(s)
    c.execute(s)
    db.commit()
    return HttpResponseRedirect("/adminsubcategory")


def adminbrand(request):
    msg = ""
    if(request.POST):
        name = request.POST['txtCategory']
        qry = f"SELECT COUNT(*) FROM `brand` WHERE `brand`='{name}'"
        c.execute(qry)
        count = c.fetchone()
        count = count[0]
        if count > 0:
            msg = "Brand already added"
        else:
            s = "insert into brand (brand) values('"+name+"')"
            try:
                c.execute(s)
                db.commit()
            except:
                msg = "Sorry some error occured"
            else:
                msg = "Brand added"
    s = "select * from brand"
    c.execute(s)
    data = c.fetchall()
    return render(request, "adminbrand.html", {"msg": msg, "data": data})


def adminnewpurchase(request):
    if request.method == "POST":
        supplier = request.POST['supplier']
        qry = f"insert into purchase_master (vid,purchase_date,total_amount) values ('{supplier}',(select sysdate()),'0')"
        c.execute(qry)
        db.commit()
        return redirect("/adminpurchaseproduct")
    qryVen = "SELECT * FROM `vendor` where `status`='Active'"
    c.execute(qryVen)
    data = c.fetchall()
    today = date.today()
    return render(request, "adminnewpurchase.html", {"data": data, "date": today})


def adminpurchaseproduct(request):
    qryPM = "select max(pm_id) from purchase_master"
    c.execute(qryPM)
    pm = c.fetchone()
    pm = pm[0]
    if "submit" in request.POST:
        item = request.POST['item']
        qty = request.POST['txtQty']
        cost = request.POST['txtCost']
        price = request.POST['txtPrice']
        selling = request.POST['txtSelling']
        qryStock = f"select rate,stock from product where pid='{item}'"
        c.execute(qryStock)
        stockDet = c.fetchone()
        stockAvail = stockDet[1]
        qryUpStock = f"insert into purchase_child(pm_id,pid,qty,rate,cost_price) values('{pm}','{item}','{qty}','{price}','{cost}')"
        c.execute(qryUpStock)
        db.commit()
        stockAvail = int(stockAvail) + int(qty)
        qryUpPro = f"update product set stock='{stockAvail}', rate='{selling}' where pid='{item}'"
        c.execute(qryUpPro)
        db.commit()
        return redirect("/adminpurchaseproduct")
    elif "complete" in request.POST:
        qry = f"select sum(rate) from purchase_child where pm_id='{pm}'"
        c.execute(qry)
        row = c.fetchone()
        total = row[0]
        qryUp = f"update purchase_master set total_amount='{total}' where pm_id='{pm}'"
        c.execute(qryUp)
        db.commit()
        return redirect("/adminnewpurchase")

    qryCat = "select * from category where `status`='Active'"
    c.execute(qryCat)
    category = c.fetchall()

    qryPro = f"SELECT product.product,purchase_child.qty,purchase_child.rate FROM product,purchase_child WHERE product.pid=purchase_child.pid AND purchase_child.pm_id='{pm}'"
    c.execute(qryPro)
    products = c.fetchall()

    qryBrand = "SELECT * FROM brand where `status`='Active'"
    c.execute(qryBrand)
    brands = c.fetchall()
    return render(request, "adminpurchaseproduct.html", {"category": category, "products": products, "brands": brands})


def adminviewpurchases(request):
    qry = "select purchase_master.*,vendor.sName,ifnull(staffs.fname,'Admin') as fname from purchase_master inner join vendor on purchase_master.vid=vendor.vid left join staffs on staffs.sid=purchase_master.sid"
    c.execute(qry)
    data = c.fetchall()
    return render(request, "adminviewpurchases.html", {"data": data})


def adminviewpurchasedetails(request):
    pmid = request.GET['pmid']
    qry = f"select product.product,purchase_child.qty,purchase_child.rate,purchase_child.pc_id,purchase_child.cost_price from product,purchase_child where product.pid=purchase_child.pid and purchase_child.pm_id='{pmid}' "
    c.execute(qry)
    data = c.fetchall()
    return render(request, "adminviewpurchasedetails.html", {"data": data})


def updatebrand(request):
    msg = ""
    cid = request.GET.get("id")
    if request.POST:
        name = request.POST['txtCategory']
        s = "update brand set brand='"+name+"' where bid='"+cid+"'"
        try:
            c.execute(s)
            db.commit()
        except:
            msg = "Sorry some error occured"
        else:
            msg = "Brand updated"
    s = "select * from brand where bid='"+cid+"'"
    c.execute(s)
    category = c.fetchall()
    s = "select * from brand where `status`='Active'"
    c.execute(s)
    data = c.fetchall()
    return render(request, "adminupdatebrand.html", {"msg": msg, "data": data, "category": category})


def deletebrand(request):
    msg = ""
    cid = request.GET.get("id")
    status = request.GET['status']
    s = f"UPDATE brand SET `status`='{status}' where `bid`='"+cid+"'"
    print(s)
    c.execute(s)
    db.commit()
    return HttpResponseRedirect("/adminbrand")


def adminproduct(request):
    msg = ""
    s = "select * from category where `status`='Active'"
    c.execute(s)
    category = c.fetchall()
    s = "select * from brand where `status`='Active'"
    c.execute(s)
    brand = c.fetchall()
    if(request.POST):
        bid = request.POST['brand']
        print(bid)
        subid = request.POST['subcat']
        product = request.POST['txtProduct']
        producdesct = request.POST['txtDesc']
        stock = request.POST['txtStock']
        rate = request.POST['txtRate']
        img = request.FILES["txtFile"]
        fs = FileSystemStorage()
        filename = fs.save(img.name, img)
        uploaded_file_url = fs.url(filename)
        s = "insert into product (subid,bid,product,description,img,stock,rate) values('"+str(
            subid)+"','"+str(bid)+"','"+product+"','"+producdesct+"','"+uploaded_file_url+"','"+stock+"','"+rate+"')"
        print(s)
        try:
            c.execute(s)
            db.commit()
        except:
            msg = "Sorry some error occured"
        else:
            msg = "Product added"
    s = "select product.*,subcategory.subcategory,category.category,brand.brand from category,subcategory,product,brand where category.catid=subcategory.catid and product.bid=brand.bid and product.subid=subcategory.subid"
    c.execute(s)
    data = c.fetchall()
    return render(request, "adminproduct.html", {"msg": msg, "data": data, "category": category, "brand": brand})


def getsub(request):
    y = request.GET.get("id")
    print(y)
    s = "select * from subcategory where catid='" + \
        str(y)+"' and `status`='Active'"
    c.execute(s)
    data = c.fetchall()
    print(data)
    jsonStr = json.dumps(data)
    print(jsonStr)
    return HttpResponse(jsonStr)


def getproduct(request):
    sid = request.GET["sid"]
    bid = request.GET["bid"]
    # qry = f"SELECT `subid` FROM `subcategory` WHERE `subcategory`='{sid}' and `status`='Active'"
    # c.execute(qry)
    # subid = c.fetchone()
    s = f"SELECT * FROM `product` WHERE `subid`='{sid}' AND `bid`='{bid}' AND `status`='Active'"
    print(s)
    c.execute(s)
    data = c.fetchall()
    print(data)
    jsonStr = json.dumps(data)
    print(jsonStr)
    return HttpResponse(jsonStr)


def updateproduct(request):
    pid = request.GET['id']
    if request.method == "POST":
        txtProduct = request.POST['txtProduct']
        txtDesc = request.POST['txtDesc']
        qryUp = f"UPDATE `product` SET `product`='{txtProduct}', `description`='{txtDesc}' WHERE `pid`='{pid}'"
        c.execute(qryUp)
        db.commit()
        return redirect("/adminproduct")
    qry = f"SELECT p.*, b.`brand`,c.`category`,s.`subcategory` FROM `product`p, `brand`b, `category`c, `subcategory`s WHERE p.`pid`='{pid}' AND p.`bid`=b.`bid` AND p.`subid`=s.`subid` AND s.`catid`=c.`catid`"
    c.execute(qry)
    data = c.fetchone()
    return render(request, "updateproduct.html", {"data": data})


def updateorderstatus(request):
    oid = request.GET['oid']
    status = request.GET['status']
    qry = f"UPDATE `order` SET `orderstatus`='{status}' WHERE `orderid`='{oid}'"
    c.execute(qry)
    db.commit()
    return redirect("/adminorders")


def cancleorder(request):
    oid = request.GET['oid']
    cchid = request.GET['cchid']
    qryOrd = f"UPDATE `order` SET `orderstatus`='Cancelled' WHERE `orderid`='{oid}'"
    c.execute(qryOrd)
    db.commit()
    qry = f"SELECT `qty`, `pid` FROM `cartchild` WHERE `cartchid`='{cchid}'"
    c.execute(qry)
    quantity = c.fetchone()
    product = quantity[1]
    quantity = quantity[0]
    qryPro = f"SELECT `stock` FROM `product` WHERE `pid`='{product}'"
    c.execute(qryPro)
    currentStock = c.fetchone()
    currentStock = currentStock[0]
    stock = int(quantity)+int(currentStock)
    qryUp = f"UPDATE `product` SET `stock`='{stock}' WHERE `pid`='{product}'"
    c.execute(qryUp)
    db.commit()
    return redirect("/customerorders?msg=Payment will be refunded within 7 days...")


def deleteproduct(request):
    msg = ""
    cid = request.GET.get("id")
    status = request.GET['status']
    s = f"UPDATE product SET `status`='{status}' where pid='"+cid+"'"
    c.execute(s)
    db.commit()
    return HttpResponseRedirect("/adminproduct")


def adminorders(request):
    s = "SELECT o.`orderdate`, o.`orderstatus`,p.`product`,p.`img`, cu.`fname`, cc.`qty`, cc.`price`, o.`orderid` FROM `order`o, `cart`c, `cartchild`cc, `product`p, `customers` cu WHERE o.`cartid`=c.`cartid` AND c.`cartid`=cc.`cartid` AND cc.`pid`=p.`pid` AND c.`cid`=cu.`cid` ORDER BY o.`orderid` DESC"
    c.execute(s)
    data = c.fetchall()
    return render(request, "adminorders.html", {"data": data})


def adminviewstaffs(request):
    s = "SELECT * FROM `staffs` WHERE `status`='Active'"
    c.execute(s)
    data = c.fetchall()
    s = "SELECT * FROM `staffs` WHERE `status`='Block'"
    c.execute(s)
    bdata = c.fetchall()
    return render(request, "adminviewstaffs.html", {"data": data, "bdata": bdata})


def adminblockstaff(request):
    sid = request.GET['sid']
    status = request.GET['status']
    s = f"UPDATE `staffs` SET `status`='{status}' WHERE `sid`='{sid}'"
    c.execute(s)
    db.commit()
    lStatus = request.GET['lStatus']
    email = request.GET['email']
    qry = f"UPDATE `login` SET `status`='{lStatus}' WHERE `username`='{email}'"
    print(qry)
    c.execute(qry)
    db.commit()
    return redirect("/adminviewstaffs")


def adminupdatestaff(request):
    sid = request.GET['sid']
    qry = f"SELECT * FROM `staffs` s, `login` l WHERE s.`email`=l.`username` AND s.`sid`='{sid}'"
    c.execute(qry)
    data = c.fetchone()
    msg = ''
    if request.method == "POST":
        fName = request.POST['fName']
        lName = request.POST['lName']
        house = request.POST['house']
        street = request.POST['street']
        district = request.POST['district']
        pin = request.POST['pin']
        contact = request.POST['contact']
        email = request.POST['email']
        password = request.POST['password']
        qryStf = f"UPDATE `staffs` SET `fname`='{fName}',`lname`='{lName}',`house`='{house}',`street`='{street}',`district`='{district}',`pincode`='{pin}',`contact`='{contact}' WHERE `sid`='{sid}'"
        c.execute(qryStf)
        db.commit()
        qryLog = f"UPDATE `login` SET `password`='{password}' WHERE `username`='{email}'"
        c.execute(qryLog)
        db.commit()
        msg = "Staff Profile Updated.."
    return render(request, "adminupdatestaff.html", {"data": data, "msg": msg})


def adminviewvendors(request):
    s = "SELECT * FROM `vendor` where `status`='Active'"
    c.execute(s)
    dataActive = c.fetchall()
    s = "SELECT * FROM `vendor` where `status`='Inactive'"
    c.execute(s)
    dataBlock = c.fetchall()
    return render(request, "adminviewvendors.html", {"dataActive": dataActive, "dataBlock": dataBlock})


def adminblockvendors(request):
    id = request.GET['id']
    status = request.GET['status']
    s = f"UPDATE `vendor` SET `status`='{status}' WHERE `vid`='{id}'"
    c.execute(s)
    db.commit()
    lStatus = request.GET['lStatus']
    email = request.GET['email']
    qry = f"UPDATE `login` SET `status`='{lStatus}' WHERE `username`='{email}'"
    print(qry)
    c.execute(qry)
    db.commit()
    return redirect("/adminviewvendors")


def adminreports(request):
    customers = ""
    staffs = ""
    vendors = ""
    purchases = ""
    orders = ""

    if request.method == "POST":
        search = request.POST['search']
        if search == "Customers":
            sDate = request.POST['sDate']
            eDate = request.POST['eDate']
            qry = f"SELECT * FROM `customers`c, `regsession`r WHERE r.`date` BETWEEN '{sDate}' AND '{eDate}' AND r.`uid`=c.`cid` AND r.`utype`='customer'"
            c.execute(qry)
            customers = c.fetchall()
        elif search == "Staffs":
            sDate = request.POST['sDate']
            eDate = request.POST['eDate']
            qry = f"SELECT * FROM `staffs`s, `regsession`r WHERE r.`date` BETWEEN '{sDate}' AND '{eDate}' AND r.`uid`=s.`sid` AND r.`utype`='staff'"
            c.execute(qry)
            staffs = c.fetchall()
        elif search == "Vendors":
            qry = f"SELECT * FROM `vendor`"
            c.execute(qry)
            vendors = c.fetchall()
        elif search == "Purchases":
            sDate = request.POST['sDate']
            eDate = request.POST['eDate']
            qry = f"SELECT purchase_master.*,vendor.sName,IFNULL(staffs.fname,'Admin') AS fname FROM purchase_master INNER JOIN vendor ON purchase_master.vid=vendor.vid AND purchase_master.`purchase_date` BETWEEN '{sDate}' AND '{eDate}'  LEFT JOIN staffs ON staffs.sid=purchase_master.sid"
            c.execute(qry)
            purchases = c.fetchall()

        elif search == "Orders":
            sDate = request.POST['sDate']
            eDate = request.POST['eDate']
            qry = f"SELECT o.`orderdate`, o.`orderstatus`,p.`product`,p.`img`, cu.`fname`, cc.`qty`, cc.`price` FROM `order`o, `cart`c, `cartchild`cc, `product`p, `customers` cu WHERE o.`cartid`=c.`cartid` AND c.`cartid`=cc.`cartid` AND cc.`pid`=p.`pid` AND c.`cid`=cu.`cid` AND o.`orderstatus`='Purchased' AND o.`orderdate` BETWEEN '{sDate}' AND '{eDate}' "
            c.execute(qry)
            orders = c.fetchall()
        elif search == "Cancelled":
            sDate = request.POST['sDate']
            eDate = request.POST['eDate']
            qry = f"SELECT o.`orderdate`, o.`orderstatus`,p.`product`,p.`img`, cu.`fname`, cc.`qty`, cc.`price` FROM `order`o, `cart`c, `cartchild`cc, `product`p, `customers` cu WHERE o.`cartid`=c.`cartid` AND c.`cartid`=cc.`cartid` AND cc.`pid`=p.`pid` AND c.`cid`=cu.`cid` AND o.`orderstatus`='Cancelled' AND o.`orderdate` BETWEEN '{sDate}' AND '{eDate}' "
            c.execute(qry)
            orders = c.fetchall()

    return render(request, "adminreports.html", {"customers": customers, "staffs": staffs, "vendors": vendors, "purchases": purchases, "orders": orders})


def staffHome(request):
    email = request.session['email']
    s = f"select * from staffs where email='{email}'"
    c.execute(s)
    d = c.fetchone()
    return render(request, "staffHome.html", {"d": d})


def customerHome(request):
    cid = request.session['id']
    s = f"SELECT * FROM `customers` WHERE `cid`='{cid}'"
    c.execute(s)
    data = c.fetchone()
    return render(request, "customerHome.html", {"data": data})


def customerviewproduct(request):
    pid = request.GET.get("id")
    cid = request.session['id']
    s = "select * from product where pid='"+pid+"'"
    c.execute(s)
    data = c.fetchall()
    rate = data[0][5]
    # print(rate)
    s = "select avg(rating) from review where pid='"+str(pid)+"'"
    c.execute(s)
    d = c.fetchone()
    rating = d[0]
    s = "select customers.fname,review.feedback from customers,review where customers.cid=review.cid and review.pid='" + \
        str(pid)+"'"
    c.execute(s)
    feedback = c.fetchall()
    if 'cart' in request.POST:
        print("-----------------------=============================-----------------")
        #################################################################
        qty = request.POST['qty']
        qry = f"select rate from product where pid='{pid}'"
        c.execute(qry)
        r = c.fetchone()
        pp = r[0]
        price = int(r[0])*int(qty)
        qry = f"select count(*) from cart where cid='{cid}' and status='In cart'"
        print(qry)
        c.execute(qry)
        r = c.fetchone()
        if(r[0] == 0):
            try:
                try:
                    qry = f"insert into cart(cid,total_amount,status) values('{cid}','0','In cart')"
                    print(qry)
                    c.execute(qry)
                    db.commit()
                except:
                    msg = "Error on cart line 603"
                    return render(request, "customerviewproduct.html", {"msg": msg})
                try:
                    qry = f"insert into cartchild(cartid,pid,qty,price,status) values((select max(cartid) from cart),'{pid}','{qty}','{price}','In cart')"
                    print(qry)
                    c.execute(qry)
                    db.commit()
                except:
                    msg = "Error on 611"
                    return render(request, "customerviewproduct.html", {"msg": msg})
                qry = "select max(cartid) from cart"
                print(qry)
                c.execute(qry)
                r = c.fetchone()
                cart_id = r[0]
                try:
                    qry = f"update cart set total_amount='price' where cartid='{cart_id}'"
                    print(qry)
                    c.execute(qry)
                    db.commit()
                except:
                    msg = "Error on 624"
                    return render(request, "customerviewproduct.html", {"msg": msg})
                return redirect("/customercart")
            except:
                msg = "One Error"
                return render(request, "customerviewproduct.html", {"msg": msg})
        else:
            qry = f"select cartid from cart where cid='{cid}' and status='In cart'"
            print(qry)
            c.execute(qry)
            r = c.fetchone()
            cart_id = r[0]
            qry = f"select count(*) from cartchild where pid='{pid}' and cartid='{cart_id}'"
            print(qry)
            c.execute(qry)
            r = c.fetchone()
            if(r[0] > 0):
                qry = f"select qty from cartchild where pid='{pid}' and cartid='{cart_id}'"
                print(qry)
                c.execute(qry)
                r = c.fetchone()
                print("=================================")
                print(qty)
                qty = int(qty)+int(r[0])
                price = pp*qty
                qry = f"select stock from product where pid='{pid}' "
                print(qry)
                c.execute(qry)
                r = c.fetchone()
                stock = r[0]
                if(qty <= stock):
                    try:
                        qry = f"update cartchild set qty='{qty}',price='{price}' where pid='{pid}' and status='In cart'"
                        print(qry)
                        c.execute(qry)
                        db.commit()
                        qry = f"select sum(price) from cartchild where cartid='{cart_id}'"
                        print(qry)
                        c.execute(qry)
                        r = c.fetchone()
                        total = r[0]
                        print(total)
                        qry = f"update cart set total_amount='{total}' where cartid='{cart_id}'"
                        print(qry)
                        c.execute(qry)
                        db.commit()
                        return redirect("/customercart")
                    except:
                        msg = "Main Error"
                        return render(request, "customerviewproduct.html", {"msg": msg})
                else:
                    msg = "Stock not available"
                    return render(request, "customerviewproduct.html", {"msg": msg})
            else:
                qry = f"select cartid from cart where cid='{cid}' and status='In cart'"
                print(qry)
                c.execute(qry)
                r = c.fetchone()
                cartid = r[0]
                qry = f"insert into cartchild(cartid,pid,qty,price,status) values('{cartid}','{pid}','{qty}','{price}','In cart')"
                print(qry)
                c.execute(qry)
                res = db.commit()
                print(res)
                db.commit()
                qry = f"select sum(price) from cartchild where cartid='{cart_id}'"
                print(qry)
                c.execute(qry)
                r = c.fetchone()
                total = r[0]
                qry = f"update cart set total_amount='{total}' where cartid='{cart_id}'"
                print(qry)
                c.execute(qry)
                db.commit()
                return redirect("/customercart")
                # else:
                #     msg = "Some Error Occured..."
                #     return render(request, "customerviewproduct.html", {"msg": msg})
                # else:
                #     msg = "Error Occured"
                #     return render(request, "customerviewproduct.html", {"msg": msg})
    ######################################################################

    elif 'review' in request.POST:
        return HttpResponseRedirect("/customerreview?id="+str(pid)+"&rating=0")
    else:
        return render(request, "customerviewproduct.html", {"data": data, "rating": rating, "feedback": feedback})


def removefromcart(request):
    chid = request.GET['chid']
    qry = f"DELETE FROM `cartchild` WHERE `cartchid`='{chid}'"
    print(qry)
    c.execute(qry)
    db.commit()
    return redirect("/customercart")


def customercart(request):
    cid = request.session['id']
    # s = "select product.pid,product.product,cart.rate,product.img from product,cart where product.pid=cart.pid and cart.cid='" + \
    #     str(cid)+"' and cart.status='In cart'"
    # c.execute(s)
    # data = c.fetchall()
    # if request.POST:
    #     return HttpResponseRedirect("/payment")
    # return render(request, "customercart.html", {"data": data})
    ########################################################################
    q = f"select total_amount,cartid from cart where cid='{cid}' and status='In cart'"
    c.execute(q)
    r = c.fetchall()
    if r:
        total = r[0]
        cartid = r[0]
        qry = f"SELECT product.*,category.category,subcategory.subcategory,brand.brand,cartchild.qty,cartchild.cartid,cartchild.cartchid, cartchild.`price` FROM category,subcategory,brand,product,cartchild,cart WHERE category.catid=subcategory.catid AND subcategory.subid=product.subid AND product.bid=brand.bid AND cartchild.pid=product.pid AND cart.cartid=cartchild.cartid AND cart.cid='{cid}' AND cartchild.status='In cart'"
        c.execute(qry)
        data = c.fetchall()
        return render(request, "customercart.html", {"data": data, "total": total})
    return render(request, "customercart.html", {"nodata": "Nodata"})


def cartupdate(request):
    cid = request.session['id']
    pid = request.GET['pid']
    rate = request.GET['rate']
    ccid = request.GET['ccid']
    qty = request.GET['qty']
    cartid = request.GET['cartid']
    newrate = int(qty) * int(rate)
    print(newrate)
    qry = f"UPDATE `cartchild` SET `qty`='{qty}', `price`='{newrate}' WHERE `cartchid`='{ccid}'"
    c.execute(qry)
    db.commit()
    qryCC = f"select sum(price) from cartchild where cartid='{cartid}'"
    c.execute(qryCC)
    r = c.fetchone()
    total = r[0]
    print(total)
    qry = f"update cart set total_amount='{total}' where cartid='{cartid}'"
    print(qry)
    c.execute(qry)
    db.commit()
    return redirect("/customercart")


def customeraddcard(request):
    cid = request.session['id']
    msg = ''
    if request.method == "POST":
        number = request.POST['number']
        name = request.POST['name']
        month = request.POST['month']
        year = request.POST['year']
        qry = f"INSERT INTO `card`(`cid`,`cardnum`,`cardname`,`expmonth`,`expyear`,`status`) VALUES ('{cid}','{number}','{name}','{month}','{year}', 'Active')"
        c.execute(qry)
        db.commit()
        msg = "Card Added..."
    qry = f"SELECT * FROM `card` WHERE `cid`='{cid}'"
    c.execute(qry)
    data = c.fetchall()
    return render(request, "customeraddcard.html", {"data": data, "msg": msg})


def customerblockcard(request):
    cardid = request.GET['id']
    status = request.GET['status']
    qry = f"UPDATE `card` SET `status`='{status}' WHERE `cardid`='{cardid}'"
    c.execute(qry)
    db.commit()
    return redirect("/customeraddcard")


def payment(request):
    cid = request.session['id']
    total = request.GET['totalValue']
    cartid = request.GET['cartid']

    if request.POST:
        cardid = request.POST['cardid']
        qryCart = f"UPDATE `cart` SET `status`='Purchased' WHERE `cartid`='{cartid}'"
        c.execute(qryCart)
        db.commit()
        qryCartChi = f"UPDATE `cartchild` SET `status`='Purchased' WHERE `cartid`='{cartid}'"
        c.execute(qryCartChi)
        db.commit()
        qryOrder = f"INSERT INTO `order` (`cartid`,`orderdate`,`orderstatus`) VALUES ('{cartid}',(select sysdate()),'Purchased')"
        c.execute(qryOrder)
        db.commit()
        qryPayment = f"INSERT INTO `payment`(`cardid`,`orderid`,`paydate`) VALUES ('{cardid}',(SELECT MAX(`orderid`) FROM `order`),(select sysdate()))"
        c.execute(qryPayment)
        db.commit()
        msg = "Payment Successful"
        qryPro = f"SELECT `pid`, `qty` FROM `cartchild` WHERE `cartid`='{cartid}'"
        c.execute(qryPro)
        products = c.fetchall()
        for p in products:
            pid = p[0]
            qty = p[1]
            qryStock = f"SELECT `stock` FROM `product` WHERE `pid`='{pid}'"
            c.execute(qryStock)
            stock = c.fetchone()
            currentStock = stock[0] - qty
            qryUp = f"UPDATE `product` SET `stock`='{currentStock}' WHERE `pid`='{pid}'"
            c.execute(qryUp)
            db.commit()
        return render(request, "payment.html", {"msg": msg})

    cDate = datetime.now()
    month = cDate.strftime("%m")
    year = cDate.strftime("%y")
    qryCard = f"SELECT * FROM `card` WHERE `cid`='{cid}' AND `status`='Active' AND (`expyear`>'{year}' OR (`expmonth`>'{month}' AND `expyear`='{year}'))"
    c.execute(qryCard)
    data = c.fetchall()
    return render(request, "payment.html", {"amt": total, "data": data})


def customerallproducts(request):
    if 'id' in request.session:
        rid = request.session['id']
    qry = "select * from category where `status`='Active'"
    c.execute(qry)
    cat = c.fetchall()
    s = "select product.*,subcategory.subcategory,category.category,brand.brand from category,subcategory,product,brand where category.catid=subcategory.catid and product.bid=brand.bid and product.subid=subcategory.subid and product.stock>0 and product.status='Active' order by product.pid desc"
    c.execute(s)
    data = c.fetchall()
    if "search" in request.POST:
        search = request.POST['search']
        s = f"SELECT product.*,subcategory.subcategory,category.category,brand.brand FROM category,subcategory,product,brand WHERE category.catid=subcategory.catid AND product.bid=brand.bid AND product.subid=subcategory.subid AND product.stock>0 AND product.status='Active' AND (category.`category` LIKE '%{search}%' OR subcategory.`subcategory` LIKE '%{search}%' OR product.`product` LIKE '%{search}%' OR product.`description` LIKE '%{search}%' OR brand.`brand` LIKE '%{search}%') ORDER BY product.pid DESC"
        c.execute(s)
        data = c.fetchall()
    if "search" in request.GET:
        search = request.GET['search']
        s = f"SELECT product.*,subcategory.subcategory,category.category,brand.brand FROM category,subcategory,product,brand WHERE category.catid=subcategory.catid AND product.bid=brand.bid AND product.subid=subcategory.subid AND product.stock>0 AND product.status='Active' AND (category.`category` LIKE '%{search}%' OR subcategory.`subcategory` LIKE '%{search}%' OR product.`product` LIKE '%{search}%' OR product.`description` LIKE '%{search}%' OR brand.`brand` LIKE '%{search}%') ORDER BY product.pid DESC"
        c.execute(s)
        data = c.fetchall()
    if "subcat" in request.POST:
        subcat = request.POST['subcat']
        s = f"SELECT product.*,subcategory.subcategory,category.category,brand.brand FROM category,subcategory,product,brand WHERE category.catid=subcategory.catid AND product.bid=brand.bid AND product.subid=subcategory.subid AND product.stock>0 AND product.status='Active' AND product.`subid`='{subcat}' ORDER BY product.pid DESC"
        c.execute(s)
        data = c.fetchall()

    return render(request, "customerallproducts.html", {"data": data, "cat": cat})


def customerreview(request):
    pid = request.GET.get("id")
    rid = request.session['id']
    rating = request.GET.get("rating")
    s = "select count(*) from review where pid='" + \
        str(pid)+"' and cid='"+str(rid)+"'"
    c.execute(s)
    d = c.fetchone()
    if d[0] > 0:
        return HttpResponseRedirect("/customerviewproduct?id="+str(pid))
    if request.POST:
        feedback = request.POST['txtfeedback']
        s = "insert into review(cid,pid,rdate,feedback,rating) values('"+str(
            rid)+"','"+str(pid)+"',(select sysdate()),'"+feedback+"','"+rating+"')"
        try:
            c.execute(s)
            db.commit()
        except:
            pass
        else:
            return HttpResponseRedirect("/customerhome")
    return render(request, "customerreview.html", {"rating": rating, "id": pid})

######################################################################


def customerorders(request):
    cid = request.session['id']
    s = f"SELECT * FROM `order`o, `cart`c, `cartchild`cc, `product`p WHERE o.`cartid`=c.`cartid` AND c.`cartid`=cc.`cartid` AND cc.`pid`=p.`pid` AND c.`cid`='{cid}' AND c.`status`='Purchased' ORDER BY o.`orderid` DESC"
    c.execute(s)
    data = c.fetchall()
    msg = ''
    if "msg" in request.GET:
        msg = request.GET['msg']
    return render(request, "customerorders.html", {"data": data, "msg": msg})


def staffVendorReg(request):
    if request.method == "POST":
        fName = request.POST['fName']
        lName = request.POST['lName']
        sName = request.POST['sName']
        street = request.POST['street']
        district = request.POST['district']
        pin = request.POST['pin']
        contact = request.POST['contact']
        email = request.POST['email']
        qryCheck = f"SELECT count(*) FROM `login`l, `customers`c, `staffs`s, `vendor`v WHERE l.`username`='{email}' OR c.`contact`='{contact}' OR s.`contact`='{contact}' OR v.`contact`='{contact}'"
        print(qryCheck)
        c.execute(qryCheck)
        check = c.fetchone()
        check = check[0]
        print(check)
        if check > 0:
            msg = "Details already registred.."
            return render(request, "staffVendorReg.html", {"msg": msg})
        else:
            qry = f"INSERT INTO `vendor` (`fName`,`lName`,`sName`,`street`,`district`,`pincode`,`contact`,`email`) VALUES ('{fName}','{lName}','{sName}','{street}','{district}','{pin}','{contact}','{email}')"
            try:
                c.execute(qry)
                db.commit()
                return redirect("vendorreg")
            except:
                msg = "Error Occured..."
                return render(request, "staffVendorReg.html", {"msg": msg})
    else:
        return render(request, "staffVendorReg.html")


def stafforders(request):
    s = "SELECT o.`orderdate`, o.`orderstatus`,p.`product`,p.`img`, cu.`fname`, cc.`qty`, cc.`price` FROM `order`o, `cart`c, `cartchild`cc, `product`p, `customers` cu WHERE o.`cartid`=c.`cartid` AND c.`cartid`=cc.`cartid` AND cc.`pid`=p.`pid` AND c.`cid`=cu.`cid` ORDER BY o.`orderid` DESC"
    c.execute(s)
    data = c.fetchall()
    return render(request, "stafforders.html", {"data": data})


def staffproduct(request):
    msg = ""
    s = "select * from category where `status`='Active'"
    c.execute(s)
    category = c.fetchall()
    s = "select * from brand where `status`='Active'"
    c.execute(s)
    brand = c.fetchall()
    if(request.POST):
        bid = request.POST['brand']
        print(bid)
        subid = request.POST['subcat']
        s = "select subid from subcategory where subcategory='"+subid+"' "
        c.execute(s)
        d = c.fetchone()
        subid = d[0]
        product = request.POST['txtProduct']
        producdesct = request.POST['txtDesc']
        img = request.FILES["txtFile"]
        fs = FileSystemStorage()
        filename = fs.save(img.name, img)
        uploaded_file_url = fs.url(filename)
        s = "insert into product (subid,bid,product,description,img) values('"+str(
            subid)+"','"+str(bid)+"','"+product+"','"+producdesct+"','"+uploaded_file_url+"')"
        print(s)
        try:
            c.execute(s)
            db.commit()
        except:
            msg = "Sorry some error occured"
        else:
            msg = "Product added"
    s = "select product.*,subcategory.subcategory,category.category,brand.brand from category,subcategory,product,brand where category.catid=subcategory.catid and product.bid=brand.bid and product.subid=subcategory.subid"
    c.execute(s)
    data = c.fetchall()
    return render(request, "staffaddproduct.html", {"msg": msg, "data": data, "category": category, "brand": brand})


def staffgetsub(request):
    y = request.GET.get("id")
    print(y)
    s = "select subcategory from subcategory where catid='" + \
        str(y)+"' and `status`='Active'"
    c.execute(s)
    data = c.fetchall()
    print(data)
    jsonStr = json.dumps(data)
    print(jsonStr)
    return HttpResponse(jsonStr)


def staffdeleteproduct(request):
    msg = ""
    cid = request.GET.get("id")
    status = request.GET['status']
    s = f"UPDATE product SET `status`='{status}' where pid='"+cid+"'"
    c.execute(s)
    db.commit()
    return HttpResponseRedirect("/staffproduct")


def staffviewvendors(request):
    s = "SELECT * FROM `vendor`"
    c.execute(s)
    data = c.fetchall()
    return render(request, "staffviewvendors.html", {"data": data})


def staffnewpurchase(request):
    if request.method == "POST":
        supplier = request.POST['supplier']
        qry = f"insert into purchase_master (vid,purchase_date,total_amount) values ('{supplier}',(select sysdate()),'0')"
        c.execute(qry)
        db.commit()
        return redirect("/staffpurchaseproduct")
    qryVen = "SELECT * FROM `vendor` where `status`='Active'"
    c.execute(qryVen)
    data = c.fetchall()
    today = date.today()
    return render(request, "staffnewpurchase.html", {"data": data, "date": today})


def staffpurchaseproduct(request):
    qryPM = "select max(pm_id) from purchase_master"
    c.execute(qryPM)
    pm = c.fetchone()
    pm = pm[0]
    if "submit" in request.POST:
        item = request.POST['item']
        qty = request.POST['txtQty']
        cost = request.POST['txtCost']
        price = request.POST['txtPrice']
        selling = request.POST['txtSelling']
        qryStock = f"select rate,stock from product where pid='{item}'"
        c.execute(qryStock)
        stockDet = c.fetchone()
        stockAvail = stockDet[1]
        qryUpStock = f"insert into purchase_child(pm_id,pid,qty,rate,cost_price) values('{pm}','{item}','{qty}','{price}','{cost}')"
        c.execute(qryUpStock)
        db.commit()
        stockAvail = int(stockAvail) + int(qty)
        qryUpPro = f"update product set stock='{stockAvail}', rate='{selling}' where pid='{item}'"
        c.execute(qryUpPro)
        db.commit()
        return redirect("/staffpurchaseproduct")
    elif "complete" in request.POST:
        qry = f"select sum(rate) from purchase_child where pm_id='{pm}'"
        c.execute(qry)
        row = c.fetchone()
        total = row[0]
        sid = request.session['id']
        qryUp = f"update purchase_master set total_amount='{total}', sid='{sid}' where pm_id='{pm}'"
        c.execute(qryUp)
        db.commit()
        return redirect("/staffnewpurchase")

    qryCat = "select * from category where `status`='Active'"
    c.execute(qryCat)
    category = c.fetchall()

    qryPro = f"SELECT product.product,purchase_child.qty,purchase_child.rate FROM product,purchase_child WHERE product.pid=purchase_child.pid AND purchase_child.pm_id='{pm}'"
    c.execute(qryPro)
    products = c.fetchall()

    qryBrand = "SELECT * FROM brand where `status`='Active'"
    c.execute(qryBrand)
    brands = c.fetchall()
    return render(request, "staffpurchaseproduct.html", {"category": category, "products": products, "brands": brands})


def staffviewpurchases(request):
    qry = "select purchase_master.*,vendor.sName,ifnull(staffs.fname,'Admin') as fname from purchase_master inner join vendor on purchase_master.vid=vendor.vid left join staffs on staffs.sid=purchase_master.sid"
    c.execute(qry)
    data = c.fetchall()
    return render(request, "staffviewpurchases.html", {"data": data})


def staffviewpurchasedetails(request):
    pmid = request.GET['pmid']
    qry = f"select product.product,purchase_child.qty,purchase_child.rate,purchase_child.pc_id,purchase_child.cost_price from product,purchase_child where product.pid=purchase_child.pid and purchase_child.pm_id='{pmid}' "
    c.execute(qry)
    data = c.fetchall()
    return render(request, "staffviewpurchasedetails.html", {"data": data})


def customergetsub(request):
    y = request.GET.get("id")
    print(y)
    s = "select * from subcategory where catid='" + \
        str(y)+"' and `status`='Active'"
    c.execute(s)
    data = c.fetchall()
    print(data)
    jsonStr = json.dumps(data)
    print(jsonStr)
    return HttpResponse(jsonStr)


def bill(request):
    oid = request.GET['oid']
    cartid = request.GET['cartid']
    id = request.session['id']
    qryOrder = f"SELECT `orderdate`,`orderstatus` FROM `order` WHERE `orderid`='{oid}'"
    c.execute(qryOrder)
    order = c.fetchone()
    qryPurchase = f"SELECT c.`total_amount`, cc.`price`, cc.`qty`, p.`product`, p.`rate` FROM `cart`c,`cartchild`cc, `product`p WHERE c.`cartid`=cc.`cartid` AND cc.`pid`=p.`pid` AND c.`cartid`='{cartid}'"
    c.execute(qryPurchase)
    purchase = c.fetchall()
    totalAmt = purchase[0][0]
    qryCustomers = f"SELECT * FROM `customers` WHERE `cid`='{id}'"
    c.execute(qryCustomers)
    customer = c.fetchone()
    return render(request, "bill.html", {"order": order, "totalAmt": totalAmt, "purchases": purchase, "customer": customer, "oid": oid})
