<template>
    <div class="container mx-auto flex">
      <img src="../assets/logo.svg" alt="logo" class="pt-3 w-13 h-13">
      <ul class="md:flex md:items-center" style="margin: 0px auto;">
        <li class="md:mx-4" v-for="link in Links">
          <a :href="link.link">{{ link.name }}</a>
        </li>
      </ul>
    </div>
</template>
  
<script>
  export default {
    setup(){
      let Links = [
        {name: "Заседание", link: "/home"},
        {name: "Добавление ППС", link: "/addPPS"},
        {name: "База шаблонов", link: "/baseShablon"},
        {name: "Черновики", link: "/chernovik"},
      ]
      return {Links}
    }
  };
</script>
  