// static/js/alerts.js

document.addEventListener('DOMContentLoaded', (event) => {
    const menuItems = {
        rs: {
            title: "Remorquage Simple",
            content: "<p>Le service de remorquage simple est conçu pour vous venir en aide lorsque votre véhicule est en panne et nécessite d'être transporté chez le garagiste de votre choix. Nos techniciens qualifiés se rendent rapidement sur les lieux de la panne pour prendre en charge votre véhicule et l'amener en toute sécurité à l'atelier du garagiste que vous avez désigné. Nous comprenons l'importance de la fiabilité et de la rapidité, c'est pourquoi nous nous engageons à offrir un service de remorquage efficace et professionnel.</p>"
        },
        rar: {
            title: "Remorquage avec Réparation",
            content: "<p>Notre service de remorquage avec réparation est la solution idéale si vous préférez confier votre véhicule à notre garage pour une réparation complète. Nous nous occupons non seulement de remorquer votre véhicule en panne, mais aussi de diagnostiquer et de réparer le problème dans notre atelier spécialisé. Notre équipe de mécaniciens expérimentés s'assurera que votre véhicule est remis en état de marche rapidement et efficacement, en utilisant des pièces de qualité et des techniques modernes de réparation.</p>"
        },
        rsp: {
            title: "Réparation sur Place",
            content: 
            "<p>Le service de réparation sur place est destiné aux situations où il est plus pratique de réparer la panne directement là où votre véhicule se trouve. Que ce soit à votre domicile, sur votre lieu de travail, ou sur le bord de la route, nos techniciens mobiles viennent à vous avec tout l'équipement nécessaire pour diagnostiquer et réparer votre véhicule sur place. Nous offrons ce service pour des pannes mineures et des problèmes mécaniques courants, afin de vous permettre de reprendre la route le plus rapidement possible.</p>"
        }
    };

    Object.keys(menuItems).forEach(id => {
        document.getElementById(id).addEventListener('click', (event) => {
            event.preventDefault();
            const service = menuItems[id];

            Swal.fire({
                title: service.title,
                html: service.content,
                showCloseButton: true,
                showCancelButton: true,
                focusConfirm: false,
                confirmButtonText: 'OK',
                cancelButtonText: 'Annuler',
                customClass: {
                    title: 'swal-title',
                    popup: 'swal-popup',
                    htmlContainer: 'swal-html-container'
                }
            });
        });
    });
});
