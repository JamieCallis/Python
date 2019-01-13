import React, {Component} from 'react'
import 'whatwg-fetch'
import cookie from 'react-cookies'
import moment from 'moment'

class PostForm extends Component {

  constructor(props) {
    super(props)
    this.handleSubmit = this.handleSubmit.bind(this)
    this.handleInputChange = this.handleInputChange.bind(this)
    this.handleDraftChange = this.handleDraftChange.bind(this)
    this.postTitleRef = React.createRef()
    this.clearForm = this.clearForm.bind(this)
    this.state = {
      title: null,
      content: null,
      draft: false,
      publish: null,
    }
  }

  updatePost(data) {
    const {post} = this.props
    const endpoint = `/api/posts/${post.slug}/`
    const csrfToken = cookie.load('csrftoken')
    let thisComp = this
    if(csrfToken !== undefined) {
      let lookupOptions = {
        method: "PUT",
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify(data),
        credentials: 'include'
      }

      fetch(endpoint, lookupOptions).then(function(response) {
        return response.json()
      }).then(function(responseData) {
        console.log(responseData)
        if (thisComp.props.postItemUpdated) {
          thisComp.props.postItemUpdated(responseData)
        }
      }).catch(function(error) {
        console.log("Error", error)
        alert("an error occured, please try again later.")
      })
    }

  }

  createPost(data) {
    // the end point
    const endpoint = '/api/posts/'
    const csrfToken = cookie.load('csrftoken')
    let thisComp = this
    if(csrfToken !== undefined) {
      let lookupOptions = {
        method: "POST",
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify(data),
        credentials: 'include'
      }

      fetch(endpoint, lookupOptions).then(function(response) {
        return response.json()
      }).then(function(responseData) {
        if (thisComp.props.newPostItemCreated) {
          thisComp.props.newPostItemCreated(responseData)
        }
        thisComp.clearForm()
      }).catch(function(error) {
        console.log("Error", error)
        alert("an error occured, please try again later.")
      })
    }

  }

  clearForm(event) {
    if(event) {
      event.preventDefault()
    }
    this.postCreateForm.reset()
    this.defaultstate();
  }

  handleSubmit(event) {
    event.preventDefault()
    let data = this.state
    const {post} = this.props
    if (post !== undefined) {
      this.updatePost(data)
    } else {
      this.createPost(data)
    }
  }

  handleInputChange(event) {
    event.preventDefault()
    let key = event.target.name
    let value = event.target.value
    if(key === 'title') {
      if(value.length > 120) {
          alert("This title is too long")
      }
    }
    this.setState({
      [key]: value
    })
  }

  handleDraftChange(event) {
    this.setState({
      draft: !this.state.draft
    })
  }

  componentDidMount() {
    const {post} = this.props
    if (post !== undefined) {
      this.setState({
          draft: post.draft,
          title: post.title,
          content: post.content,
          publish: moment(post.publish).format('YYYY-MM-DD'),
      })
    } else {
      this.setState({
          draft: false,
          title: null,
          content: null,
          publish: null,
          publish: moment(new Date()).format('YYYY-MM-DD'),
      })
    }

    // this.postTitleRef.current.focus()
  }

  render() {
    const {publish} = this.state
    const {title} = this.state
    const {content} = this.state
    return (
        <form onSubmit={this.handleSubmit} ref={(el) => this.postCreateForm = el}>
            <div className='form-group'>
                <label for='title'>Post Title</label>
                <input
                  type='text'
                  id='title'
                  name='title'
                  value={title}
                  className='form-control'
                  ref = {this.postTitleRef}
                  placeholder='Blog post title'
                  onChange={this.handleInputChange} required/>
            </div>
            <div className='form-group'>
                <label for='content'>Content</label>
                <textarea
                  id='content'
                  name='content'
                  className='form-control'
                  placeholder='Post Content'
                  value={content}
                  onChange={this.handleInputChange}
                  required
                  />
            </div>
            <div className='form-group'>
                <label for='draft'>
                <input
                  type='checkbox'
                  id='draft'
                  name='draft'
                  value={this.state.draft}
                  // checked ={this.state.draft}
                  onChange={this.handleDraftChange}
                  />
                Draft
                </label>
            </div>
            <div className='form-group'>
                <label for='publish'>Publish Date</label>
                <input
                  type='date'
                  id='publish'
                  name='publish'
                  className='form-control'
                  value={publish}
                  onChange={this.handleInputChange}
                  required
                  />
            </div>
            <button className='btn btn-primary'>Save</button>
            <button className={`btn btn-secondary`} onClick={this.clearForm}>Clear</button>
        </form>
    )
  }
}

export default PostForm
