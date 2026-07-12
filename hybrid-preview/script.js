const pricingStyles=document.createElement('link');pricingStyles.rel='stylesheet';pricingStyles.href='packages-update.css';document.head.appendChild(pricingStyles);
const mobileStyles=document.createElement('link');mobileStyles.rel='stylesheet';mobileStyles.href='mobile.css';document.head.appendChild(mobileStyles);

const state={vehicle:'Small Car',service:'Jacky Jones Special Package',condition:'Moderate'};

const priceMatrix={
  'Vacuum & Wash/Wax':{
    'Small Car':60,
    'SUV or Truck':75,
    'Big Rig':90,
    'RV':90,
    'Tandem Axle Trailer':90
  },
  'Deluxe Package':{
    'Small Car':85,
    'SUV or Truck':100
  },
  'Jacky Jones Special Package':{
    'Small Car':150,
    'SUV or Truck':200,
    'Big Rig':250,
    'RV':250,
    'Tandem Axle Trailer':250
  }
};

const serviceContent={
  detail:{kicker:'Refresh. Clean. Renew.',title:'Bring back a clean, comfortable vehicle.',description:'From a vacuum, wash, and wax to a complete top-to-bottom detail, choose the level of care your vehicle needs.',items:['Vacuum & Wash/Wax','Deluxe Package','Jacky Jones Special Package','Large and specialty vehicles'],image:'../assets/services-panel.jpg',alt:'Detailed black performance vehicle',choice:'Jacky Jones Special Package'},
  enhance:{kicker:'Restore. Correct. Refine.',title:'Improve clarity, gloss, and finish.',description:'Paint enhancement and correction services target oxidation, haze, swirls, and other visible defects.',items:['Gloss enhancement','Paint correction','Headlight restoration','Finish consultation'],image:'../assets/poster-detail.jpg',alt:'BoPeePs paint enhancement promotional image',choice:'Paint Correction'},
  protect:{kicker:'Seal. Protect. Maintain.',title:'Make the finish easier to maintain.',description:'Protection services add gloss and help shield exterior surfaces from everyday contamination.',items:['Premium wax','Paint sealants','Ceramic preparation','Maintenance recommendations'],image:'../assets/social-card.jpg',alt:'BoPeePs protection promotional image',choice:'Protection'}
};

function getPublishedPrice(){
  const packagePrices=priceMatrix[state.service]||{};
  const price=packagePrices[state.vehicle];
  return Number.isFinite(price)?price:null;
}

function ensureEstimateRow(){
  const summaryList=document.querySelector('.quote-summary dl');
  if(!summaryList||summaryList.querySelector('[data-estimate]'))return;
  const row=document.createElement('div');
  row.className='estimate-row';
  row.innerHTML='<dt>Published price</dt><dd data-estimate></dd>';
  summaryList.appendChild(row);
  const note=document.createElement('p');
  note.className='estimate-note';
  note.textContent='Final price is confirmed before service and may vary with vehicle size, condition, or added work.';
  summaryList.insertAdjacentElement('afterend',note);
}

function updateEstimate(){
  ensureEstimateRow();
  const estimate=document.querySelector('[data-estimate]');
  if(!estimate)return;
  const price=getPublishedPrice();
  estimate.textContent=price===null?'Custom quote':`From $${price}`;
}

function syncSummary(){
  Object.entries(state).forEach(([key,value])=>{
    document.querySelectorAll(`[data-summary="${key}"]`).forEach(el=>el.textContent=value);
    document.querySelectorAll(`[data-form-field="${key}"]`).forEach(el=>el.value=value);
  });
  updateEstimate();
}

function selectChoice(group,button){
  document.querySelectorAll(`[data-choice-group="${group}"] .choice`).forEach(item=>item.classList.toggle('is-selected',item===button));
  state[group]=button.dataset.value;
  syncSummary();
}

document.querySelectorAll('[data-choice-group]').forEach(group=>{
  group.addEventListener('click',event=>{
    const button=event.target.closest('.choice');
    if(button)selectChoice(group.dataset.choiceGroup,button);
  });
});

document.querySelectorAll('[data-service-tab]').forEach(tab=>{
  tab.addEventListener('click',()=>{
    const content=serviceContent[tab.dataset.serviceTab];
    document.querySelectorAll('[data-service-tab]').forEach(item=>{
      const selected=item===tab;
      item.classList.toggle('is-active',selected);
      item.setAttribute('aria-selected',String(selected));
    });
    document.querySelector('[data-service-kicker]').textContent=content.kicker;
    document.querySelector('[data-service-title]').textContent=content.title;
    document.querySelector('[data-service-description]').textContent=content.description;
    document.querySelector('[data-service-list]').innerHTML=content.items.map(item=>`<li>${item}</li>`).join('');
    const image=document.querySelector('[data-service-image]');
    image.src=content.image;
    image.alt=content.alt;
    const choose=document.querySelector('[data-service-choose]');
    choose.textContent=`Choose ${tab.textContent.trim().split(/\s+/)[0]}`;
    choose.dataset.choice=content.choice;
  });
});

document.querySelector('[data-service-choose]')?.addEventListener('click',event=>{
  state.service=event.currentTarget.dataset.choice||'Jacky Jones Special Package';
  syncSummary();
  document.querySelector('#builder').scrollIntoView({behavior:'smooth'});
});

document.querySelectorAll('[data-package]').forEach(button=>{
  button.addEventListener('click',()=>{
    state.service=button.dataset.package;
    syncSummary();
    document.querySelector('#builder').scrollIntoView({behavior:'smooth'});
  });
});

document.querySelector('[data-continue-quote]')?.addEventListener('click',()=>document.querySelector('[data-quote-form]').scrollIntoView({behavior:'smooth'}));

function quoteLines(form){
  const data=new FormData(form);
  const price=getPublishedPrice();
  return[
    'Hi BoPeePs, I would like a detailing quote.',
    `Name: ${data.get('name')||''}`,
    `Phone: ${data.get('phone')||''}`,
    `Email: ${data.get('email')||'Not provided'}`,
    `Vehicle: ${data.get('vehicleModel')||''}`,
    `Vehicle type: ${data.get('vehicleType')||state.vehicle}`,
    `Service: ${data.get('service')||state.service}`,
    `Published price shown: ${price===null?'Custom quote':`$${price}`}`,
    `Condition: ${data.get('condition')||state.condition}`,
    `Notes: ${data.get('notes')||'No additional notes'}`
  ];
}

const form=document.querySelector('[data-quote-form]');
const status=document.querySelector('[data-form-status]');

function openTextQuote(number,label){
  if(!form.reportValidity())return;
  status.textContent=`Opening your text app for the ${label} line. You can attach photos before sending.`;
  window.location.href=`sms:${number}?body=${encodeURIComponent(quoteLines(form).join('\n'))}`;
}

form?.addEventListener('submit',event=>{
  event.preventDefault();
  openTextQuote('+17068976177','706');
});

function addSecondaryTextButton(){
  const actions=form?.querySelector('.form-actions');
  if(!actions||actions.querySelector('[data-text-secondary]'))return;
  const button=document.createElement('button');
  button.className='button button-ghost';
  button.type='button';
  button.dataset.textSecondary='';
  button.textContent='Text 850 Line';
  const emailButton=actions.querySelector('[data-email-quote]');
  actions.insertBefore(button,emailButton);
  button.addEventListener('click',()=>openTextQuote('+18503485791','850'));
}

addSecondaryTextButton();

document.querySelector('[data-email-quote]')?.addEventListener('click',()=>{
  if(!form.reportValidity())return;
  status.textContent='Opening your email app.';
  const subject=encodeURIComponent('BoPeePs Detailing Quote Request');
  const body=encodeURIComponent(quoteLines(form).join('\n'));
  window.location.href=`mailto:bopeepsdetail@gmail.com?subject=${subject}&body=${body}`;
});

const header=document.querySelector('[data-header]');
const menuButton=document.querySelector('[data-menu-button]');
const nav=document.querySelector('[data-nav]');
function setHeader(){header?.classList.toggle('scrolled',window.scrollY>12)}
function closeMenu(){
  nav?.classList.remove('is-open');
  menuButton?.setAttribute('aria-expanded','false');
  header?.classList.remove('open');
}
setHeader();
window.addEventListener('scroll',setHeader,{passive:true});
menuButton?.addEventListener('click',()=>{
  const open=nav.classList.toggle('is-open');
  menuButton.setAttribute('aria-expanded',String(open));
  menuButton.setAttribute('aria-label',open?'Close menu':'Open menu');
  header.classList.toggle('open',open);
});
nav?.addEventListener('click',event=>{
  if(event.target.matches('a'))closeMenu();
});
document.addEventListener('keydown',event=>{
  if(event.key==='Escape'){
    closeMenu();
    menuButton?.focus();
  }
});
document.addEventListener('click',event=>{
  if(nav?.classList.contains('is-open')&&!header?.contains(event.target))closeMenu();
});
window.addEventListener('resize',()=>{
  if(window.innerWidth>1020)closeMenu();
});

syncSummary();