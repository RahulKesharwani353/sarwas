// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDJLhX6ApFxMb_A0Y2QjMs-MvySnxoDv4o",
  authDomain: "shareilii.firebaseapp.com",
  databaseURL: "https://shareilii-default-rtdb.firebaseio.com",
  projectId: "shareilii",
  storageBucket: "shareilii.appspot.com",
  messagingSenderId: "717315171099",
  appId: "1:717315171099:web:d0503ecfd2dc2e6705e9be",
  measurementId: "G-PP2JTFFG1E"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);