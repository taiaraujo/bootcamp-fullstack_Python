const pets = [
    {
        name : 'rex',
        type : 'dog',
        age: 10,
        weight: 5
    },
    {
        name : 'spike',
        type : 'dog',
        age: 8,
        weight: 5
    },
    {
        name : 'booble',
        type : 'cat',
        age: 2,
        weight: 3.6
    },
    {
        name : 'tom',
        type : 'cat',
        age: 6,
        weight: 3
    },
    {
        name : 'gulp',
        type : 'fish',
        age: 1,
        weight: 0.6
    },
    {
        name : 'Seringuejo',
        type : 'crap',
        age: 1,
        weight: 0.9
    }
]

console.log("\nArray inicial\n")
console.log(pets)

const olderThen5 = (number) => {
    return number < 5
}

/**
 * FILTER
 * Retornar um novo array na qual o elemento que passe pela função e
 * retorne True
 */
const newPets = pets.filter( ({age}) => olderThen5(age) )

console.log("\nResultado do Filter\n")
console.log(newPets)

/**
 * MAP
 * Retornar um novo array com a mesma quantidade de elementos
 * que o array principal
 */
const petNames = pets.map( (pet) => {return pet.name})

console.log("\nResultado do Map\n")
console.log(petNames)

/**
 * Foreach
 * Não retorna um novo array com a mesma quantidade de elementos
 */
const foreachPetNames = []

pets.forEach( (pet) => { return foreachPetNames.push(pet.name) });

console.log("\nResultado Foreach\n")
console.log(foreachPetNames)

/**
 * REDUCE
 * Executa uma função para cada elemento retornando um
 * único valor de retorno
 */
const totalWeitght = pets.reduce( (total, pet) => {
    return{
        totalAge: total.totalAge + pet.age,
        totalWeitght: total.totalWeitght + pet.weight
    }
}, { totalAge: 0, totalWeitght: 0 } )

console.log("\n Resultado Reduce\n")
console.log(totalWeitght)


// exemplo B (peso apenas dos 'dogs') com REDUCE
const DogsWeitght = pets.reduce( (total, pet) => {
    if (pet.type !== 'dog') return total
    
    return total + pet.weight
}, 0)

console.log("\nResultado peso dos cães com Reduce\n")
console.log(DogsWeitght)


// exemplo b com filter
const dogsFilter = pets.filter( (pet) => {
    return pet.type === 'dog'
} )

console.log("\nResultado somente cães com Filter\n")
console.log(dogsFilter)

const DogsWeitghtReduce = dogsFilter.reduce( (total, pet) => {
    return total + pet.weight
}, 0)

console.log("\nResultado peso dos cães com Reduce de um Filter\n")
console.log(DogsWeitghtReduce)

// encadeando filter e reduce
const dogsFilterReduce = pets.filter( (pet) => {
    return pet.type === 'dog'
} ).reduce( (total, pet) => {
    return total + pet.weight
}, 0)

console.log("\nResultado peso dos cães com encadeamento de Filter e Reduce\n")
console.log(dogsFilterReduce)

// exemplo com promise
const items = ['a', 'b', 'c', 'd', 'e']

;(async function (){
    const promiseFunction = async (element) => {
        return new Promise( (resolve, reject) => {
            return resolve( `${element} - promise` )
        } )
    }

    const itemsMappedPromises = items.map(promiseFunction)

    const itemsMapped = await Promise.all(itemsMappedPromises)

    console.log(itemsMapped)

} )() 