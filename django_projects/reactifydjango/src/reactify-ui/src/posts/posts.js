import React, { Component } from 'react';
import 'whatwg-fetch'
import cookie from 'react-cookies'


class Posts extends Component {
  loadPosts() {
    // the end point
    const endpoint = '/api/posts'

    let lookupOptions = {
      method: "GET",
      headers: {
        'Content-Type': 'application/json'
      }
    }

    fetch(endpoint, lookupOptions).then(function(response) {
      return response.json()
    }).then(function(responseData) {
      console.log(responseData)
    }).catch(function(error) {
      console.log("Error", error)
    })
  }

  render() {
    return (
      <h1> Post component </h1>
    );
  }
}

export default Posts;
