# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 15:16:36 2021

@author: 91700
"""
from flask import Flask,request,redirect,url_for
from flask import jsonify
from collections import OrderedDict

app=Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

def find_parents(list_process,first_value,queue_list):
    list_append=[]
    for each_relation in list_process:
        if each_relation["child"]==first_value:
            if each_relation["parent"] not in queue_list:
                list_append.append(each_relation["parent"])
    return list_append


def path_list(list_process,node):
    queue_list=[]
    stack_list=[]
    queue_list.append(node)
    while(len(queue_list)!=0):
        first_value=queue_list.pop(0)
        stack_list.insert(0,first_value)
        list_append=find_parents(list_process,first_value,queue_list)
        queue_list.extend(list_append)
        
    return stack_list


@app.route('/',methods= ['POST','GET'])
def accept_post():
    if request.method=='POST':
        content=request.get_json(silent=False)
        list_input=content['relation']
        process_input=content['node_ids']
        list_process=list_input[::-1]
        output_dict=OrderedDict()
        for i in process_input:
            output_dict[i]=path_list(list_process,i);
        print(output_dict)
        return jsonify(output_dict)
    else:
        s="----GET request response recieved---- --> POST a JSON data to receive output in JSON"
        return jsonify(s)
        




if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)