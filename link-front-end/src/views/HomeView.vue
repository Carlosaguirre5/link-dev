<script setup>
  import { ref } from "vue"
  import { useRouter } from "vue-router"
  const router = useRouter()
  const input = ref("")

  const handleEnterKey = () => {
    if (input.value !== "steven") {
        input.value = ""
        alert("campo reiniciado")
    }else{
        router.push("inventario")
    }
  }
</script>
<template>
  <main class="main">
    <div style="margin-bottom: 50px;">Link la mejor plataforma</div>
    <div class="input">
      <input type="password" v-model="input" @keyup.enter.prevent="handleEnterKey" placeholder="your secret key"/>
    </div>
  </main>
</template>


<style scoped lang="scss">
  .text-center {
    & .v-field__input {
      text-align: center;
    }
  }

  .main {
    display: flex;
    flex-direction: column;
    height: calc(100vh - 4rem);
    place-content: center;
    place-items: center;
  }

  input{
    width: 100%;
    outline-style: solid;
    outline-width: 0.001em;
    border-radius: 5px;
    padding: 0.8rem 1rem;
    text-align: center;
    color: rgba(250, 235, 215, 0.661);
    outline-color: rgba(250, 235, 215, 0.222);
    transition: outline-color 0.3s;
    &::placeholder{
      color: rgba(250, 235, 215, 0.479);
    }
    &:focus{
      outline-width: 2px;
      outline-color: rgba(250, 235, 215, 0.774);
    }
    &:hover{
      outline-color: rgba(250, 235, 215, 0.774);
      transition: outline-color 0.3s;
    }
  }

  .input {
    display: flex;
    flex-direction: column;
    place-items: center;
    min-width: 30rem;
  }

  @media (width > 876px) {
    .input {
      margin-bottom: 200px;
    }
  }
</style>
