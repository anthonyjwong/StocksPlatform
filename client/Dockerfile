# pull official base image
FROM node:13.12.0-alpine

# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# add app
COPY . ./


# install app dependencies
COPY package.json ./
RUN npm install --force
RUN npm install react-scripts@3.4.1 -g --silent

# default port for react
EXPOSE 3000

# start app
CMD ["npm", "start"]
