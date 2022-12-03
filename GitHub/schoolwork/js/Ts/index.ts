type employee = {
    readonly id: number,
    name: string
    retire: (data: Date) => void
}

let Employee: employee = {
    id: 1,
    name: 'Mosh',
    retire: (date: Date) => {
        console.log(date);
    }
}