
console.log("your javascript")

document.addEventListener('DOMContentLoaded', (event) => {
	var coll = document.getElementsByClassName('collapsible')
	var i
  
	for (i = 0; i < coll.length; i++) {
	  coll[i].addEventListener('click', function () {
		this.classList.toggle('active')
		var content = this.nextElementSibling
		if (content.style.maxHeight) {
		  content.style.maxHeight = null
		} else {
		  content.style.maxHeight = content.scrollHeight + 'px'
		}
	  })
	}
  })
  
  console.log('hi javascript is working in index file')
  const navlink = document.querySelectorAll('.nav a')
  navlink.forEach((navlink) => {
	navlink.addEventListener('click', () => {
	  document.querySelector('.active')?.classList.remove()('.active')
	  navlink.classList.add('.active')
	})
  })