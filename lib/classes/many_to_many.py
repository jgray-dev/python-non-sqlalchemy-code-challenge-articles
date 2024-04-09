class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    def get_title(self):
        return self._title

    def set_title(self, value):
        if type(value) is str:
            if 5 <= len(value) <= 50:
                if not hasattr(self, "_title"):
                    self._title = value
                else:
                    raise Exception("Title is already defined")
            else:
                raise Exception("Title length must be between 5 and 50 characters")
        else:
            raise Exception("Title must be of type string")

    title = property(get_title, set_title)

    def get_author(self):
        return self._author

    def set_author(self, value):
        if type(value) is Author:
            self._author = value
        else:
            raise Exception("Author must be of type Author")

    author = property(get_author, set_author)

    def get_magazine(self):
        return self._magazine

    def set_magazine(self, value):
        if type(value) is Magazine:
            self._magazine = value
        else:
            raise Exception("Magazine must be of type Magazine")

    magazine = property(get_magazine, set_magazine)


class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def get_name(self):
        return self._name

    def set_name(self, value):
        if type(value) is str:
            if len(value) > 0:
                if not hasattr(self, "_name"):
                    self._name = value
                else:
                    raise Exception("Name is already defined")
            else:
                raise Exception("Name length must be greater than 0")
        else:
            raise Exception("Name must be of type string")

    name = property(get_name, set_name)

    def articles(self):
        return [article for article in Article.all if article.author is self]

    def magazines(self):
        return list({article.magazine for article in Article.all if article.author is self})

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        return new_article

    def topic_areas(self):
        returnList = set()
        for article in Article.all:
            if article.author is self:
                returnList.add(article.magazine.category)
        if len(returnList) > 0:
            return list(returnList)
        else:
            return None


class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    def get_name(self):
        return self._name

    def set_name(self, value):
        if type(value) is str:
            if 16 >= len(value) >= 2:
                self._name = value
            else:
                raise Exception("Name length must be between 2 and 16 characters")
        else:
            raise Exception("Name must be of type string")

    name = property(get_name, set_name)

    def get_category(self):
        return self._category

    def set_category(self, value):
        if type(value) is str:
            if len(value) > 0:
                self._category = value
            else:
                raise Exception("Name length must be greater than 0")
        else:
            raise Exception("Name must be of type string")

    category = property(get_category, set_category)

    def articles(self):
        return [article for article in Article.all if article.magazine is self]

    def contributors(self):
        return list({article.author for article in Article.all if article.magazine is self})

    def article_titles(self):
        returnList = list()
        for article in Article.all:
            if article.magazine is self:
                returnList.append(article.title)
        if len(returnList) > 0:
            return returnList
        return None

    def contributing_authors(self):
        returnList = list()
        for author in Author.all:
            temp = 0
            for article in Article.all:
                if article.author is author and article.magazine is self:
                    temp += 1
            if temp > 2:
                returnList.append(author)
        if len(returnList) > 0:
            return returnList
        return None

    @classmethod
    def top_publisher(cls):
        maxAmt = 0
        topPub = None
        for magazine in Magazine.all:
            temp = 0
            for article in Article.all:
                if article.magazine is magazine:
                    temp += 1
            if temp > maxAmt:
                maxAmt = temp
                topPub = magazine
        return topPub
