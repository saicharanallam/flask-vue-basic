<template>
  <div>
    <h1>I Can make the bad guys good for a weekend!!!</h1>
    <div class="container">
      <button type="button" class="btn btn-primary">{{ msg }}</button></div>
    <p>Lets see if this works!</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Ping',
  data() {
    return {
      msg: 'Hello!',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/ping';
      axios
        .get(path)
        .then((res) => {
          this.msg = res.data;
          console.log(res);
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
