--Contact 

create table Contact(
    id INTEGER PRIMARY KEY,
    userName VARCHAR(50) NOT NULL,
    userPhone INTEGER NOT NULL,
    userEmail VARCHAR(30) NOT NULL,
    subject VARCHAR(50) NOT NULL,
    userMessage VARCHAR(100),
    messageDate VARCHAR(10)
)
INSERT INTO Contact(userName,userPhone,userEmail,subject,userMessage)
VALUES ("Yusif",0556515252,"yusif@gmail.com","Blogs","Can you share my states in your website ?")

SELECT * from Contact;

-- Blogs comment information  Reply 
create TABLE Comment(
    id INTEGER primary KEY,
    userName VARCHAR(50) NOT NULL,
    userEmail VARCHAR(30) NOT NULL,
    userMessage VARCHAR(100),
    commetDate DATETIME
)

INSERT INTO COMMENT(userName,userEmail,userMessage)
VALUES ("Yusif","yusif@gmail.com","Perfect state about SQL joins!")

SELECT * from COMMENT;

-- Blog inner page
create TABLE innerBlog(
    id INTEGER primary KEY,
    blogTitle VARCHAR(30) Not NULL,
    blogDate VARCHAR(15) NOT NULL,
    blogImgUrl VARCHAR(100),
    blogContent VARCHAR(300)
)
INSERT into innerBlog(blogTitle, blogDate,blogImgUrl,blogContent)
VALUES ("SQL Joins", "datatime('now')","/img/blog1.png","INNER JOIN: LEFT JOIN: RIGHT JOIN: OUTER JOIN")

SELECT * FROM innerBlog;