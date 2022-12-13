
import React, {useEffect, useReducer, useState } from 'react';
import axios from 'axios'; 
// import Popup from 'reactjs-popup';
import 'reactjs-popup/dist/index.css';
import './Update.css'

function Update(props) {
  const MY_SERVER = 'http://localhost:5000/todos/'

  const [title, setTitle] = useState('')
  const [desc, setDesc] = useState('')

  // if (props.trigger){
  //   setDesc(props.object.desc)
  //   setTitle(props.object.title)
  // }
  useEffect(()=> {
    console.log(props.object_id)
  //   if (props.trigger){
  //   setDesc(props.object.desc)
  //   setTitle(props.object.title)
  // }

  },[]);

  const done = async(id) => {
    if (title){
      const response = await axios.put(MY_SERVER+id, {title:title.trim(), desc:desc.trim()})
      setTitle('')
      setDesc('')
      props.loadData()
      props.setTrigger(false)
      return response.data
    }
    else{
      console.log('You need a title')
    }
    
  }

  return (props.trigger) ?(
    <div className='Update'>
        <div className='Update-inner'>
            <div className="modal-dialog" role="document">
              <div className="modal-content">
                <div className="modal-header">
                  <h5 className="modal-title" id="exampleModalLabel">Edit task "{props.object_id}"</h5>
                  <button type="button" onClick={() => props.setTrigger(false)} className="close btn" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                  </button>
                </div>
                <div className="modal-body mb-3">
                  <form>
                    <div className="form-group">
                      <label htmlFor="recipient-name" className="col-form-label">Title:</label>
                      <input type="text" className="form-control" value={title} onChange={(e) => setTitle(e.target.value)} id="recipient-name"/>
                    </div>
                    <div className="form-group">
                      <label htmlFor="message-text" className="col-form-label">Content:</label>
                      <textarea className="form-control" value={desc} onChange={(e) => setDesc(e.target.value)} id="message-text"></textarea>
                    </div>
                  </form>
                </div>
                <div className="modal-footer">
                  <button type="button" onClick={() => props.setTrigger(false)} className="p-2 px-4 mx-2 btn btn-secondary" data-dismiss="modal">Close</button>
                  <button type="button" onClick={() => done(props.object_id)} className="p-2 px-5 mx-2  btn btn-primary">Done</button>
                </div>
              </div>
            </div>
          </div>
        {/* <Popup trigger={<button> Trigger</button>} position="right center">
        <button type="button"  onClick={() => props.setTrigger(false)} className="btn btn-secondary">
          close
          </button>
        <div>Popup content here !!</div>
        {/* </Popup> */}
      </div>
    
  ):"";
}

export default Update