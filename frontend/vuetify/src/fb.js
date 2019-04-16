import firebase from 'firebase/app'
import 'firebase/firestore'

// Initialize Firebase
var config = {
  apiKey: "AIzaSyCyrV2vFnKFbiNYePizWCcGLwfD9Bb2-sU",
  authDomain: "todo-vuetify-e8d97.firebaseapp.com",
  databaseURL: "https://todo-vuetify-e8d97.firebaseio.com",
  projectId: "todo-vuetify-e8d97",
  storageBucket: "todo-vuetify-e8d97.appspot.com",
  messagingSenderId: "931988885912"
};
firebase.initializeApp(config);
const db = firebase.firestore();

db.settings({ timestampsInSnapshots: true});

export default db;