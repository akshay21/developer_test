def template(source_template, req_id):
    
    template = str(source_template)

    return template.format(CODE=str(req_id), ALTCODE=str(req_id)[0:5] + "-" + str(req_id)[5:8])


