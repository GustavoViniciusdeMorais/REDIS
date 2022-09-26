FROM python:3.7-alpine
WORKDIR /code
RUN pip install flask
RUN pip install redis
RUN pip install jsonify
EXPOSE 8000
ENTRYPOINT ["tail", "-f", "/dev/null"]
# ENTRYPOINT [ "python" ] 
# CMD [ "app.py" ]