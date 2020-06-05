# 588. Design In-Memory File System

# Design an in-memory file system to simulate the following functions:

# ls: Given a path in string format. If it is a file path, return a list that only contains this file's name. If it is a directory path, return the list of file and directory names in this directory. Your output (file and directory names together) should in lexicographic order.

# mkdir: Given a directory path that does not exist, you should make a new directory according to the path. If the middle directories in the path don't exist either, you should create them as well. This function has void return type.

# addContentToFile: Given a file path and file content in string format. If the file doesn't exist, you need to create that file containing given content. If the file already exists, you need to append given content to original content. This function has void return type.

# readContentFromFile: Given a file path, return its content in string format.

 

# Example:

# Input: 
# ["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]
# [[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]

# Output:
# [null,[],null,null,["a"],"hello"]

# https://assets.leetcode.com/uploads/2018/10/12/filesystem.png


from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.content = ""
        
class FileSystem(object):

    def __init__(self):
        self.root = TrieNode()
    
    #find and return TrieNode at path.
    def find(self, path):
        curr = self.root
        # no nested path
        if len(path) == 1:
            return self.root
        for word in path.split("/")[1:]:
            curr = curr.children[word]
        return curr
        
    def ls(self, path):
        curr = self.find(path)
        # file path, return file name if curr is a file
        if curr.content:
            return [path.split('/')[-1]]
        # if directory, return children keys
        return sorted(curr.children.keys())
		
    def mkdir(self, path):
        self.find(path)

    def addContentToFile(self, filePath, content):
        curr = self.find(filePath)
        curr.content += content

    def readContentFromFile(self, filePath):
        curr = self.find(filePath)
        return curr.content