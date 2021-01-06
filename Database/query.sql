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

//Project files
CREATE TABLE projectFiles(
    id integer PRIMARY KEY,
    fileName VARCHAR(50),
    fileType VARCHAR(50),
    fileUrl VARCHAR(50)
)
INSERT into projectFiles(fileName, fileType,fileUrl)
VALUES("portfolioImg","svg","img/portImg6")
SELECT * from projectFiles;
//Portfolio

create table Portfolio(
    id integer primary KEY,
    portfolioName VARCHAR(30),
    portfolioCategory integer,
    portfolioStatus BOOLEAN,
    CONSTRAINT portfolioCategory
    FOREIGN KEY (portfolioCategory)
    REFERENCES portfolioCategory(id)
)
INSERT INTO Portfolio(portfolioName,portfolioCategory,portfolioStatus)
VALUES("Korea",2,"True")

select * from Portfolio;
SELECT Portfolio.id,portfolioName,categoryName,portfolioStatus 
from Portfolio
INNER JOIN portfolioCategory on portfolioCategory = portfolioCategory.id;




CREATE TABLE portfolioFiles(
    id integer PRIMARY KEY,
    portfolioId integer,
    projectFilesId integer,
    CONSTRAINT portfolioFilesPortfolio
    FOREIGN KEY (portfolioId)
    REFERENCES Portfolio(id)
    CONSTRAINT portfolioFilesProjectFiles
    FOREIGN KEY (projectFilesId)
    REFERENCES projectFiles(id)
)
insert into portfolioFiles(portfolioId,projectFilesId)
VALUES (1,2),(1,4),(3,6),(3,8),(5,5),(5,6),(2,2)
select * from portfolioFiles;

CREATE TABLE portfolioCategory(
    id integer primary KEY,
    categoryName VARCHAR(20)
)

INSERT into portfolioCategory (categoryName)
VALUES ("Apple"),("Samsung"),("Nokia") 
SELECT * from portfolioCategory;

SELECT Portfolio.id,portfolioName,categoryName,fileName,fileType,fileUrl,portfolioStatus 
from Portfolio
INNER JOIN portfolioFiles on Portfolio.id = portfolioFiles.portfolioId
INNER JOIN projectFiles on portfolioFiles.projectFilesId = projectFiles.id
INNER JOIN portfolioCategory on portfolioCategory = portfolioCategory.id  