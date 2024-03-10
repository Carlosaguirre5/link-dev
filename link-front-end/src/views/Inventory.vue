<script setup>
    import { ref, onMounted } from "vue"
    import { useRouter } from "vue-router"
    const router = useRouter()
    import "./styles/inventory.scss"
    import Card from "../components/Card.vue"

    const items = ref(null)
    const loading = ref(false)
    const button = ref(false)
    // cosnt handleClick = ()=>{
    //     router.push("/vue")
    // }

    async function fetchData() {
        try {
            loading.value = true
            const response = await fetch('/apilink/dev/inventario');
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            const data = await response.json();
            items.value = data; // Assuming the response is an array of items
            console.log(items || "aun no")
        } catch (error) {
            console.error('There was a problem fetching the data:', error);
        } finally {
            loading.value = false
        }
    }
    onMounted(fetchData)
</script>

<template>
    <div>
        <div v-if="loading" class="container">
            Cargandooo...
        </div>
        <div v-else class="container">
            <div v-for="item in items" :key="item._id.$oid">
                <Card :link="item.link" :marca="item.marca" :modelo="item.modelo" :rese="item.rese" />
            </div>
            <v-btn ref="button" @click="handleClick">Salir</v-btn>
        </div>
    </div>
</template>

<style scoped lang="scss">
    .container {
        display: flex;
        justify-content: center;
        gap: 2rem
    }
</style>
