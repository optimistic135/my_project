import{_ as d,r as t,o as _,c as m,a as n,w as s,b as h,d as a}from"./index-49d31e09.js";const x={data(){return{input:"",data:null}},methods:{exer(){this.input===null||this.input.trim()===""||isNaN(this.input)||this.input<1||this.input>5556?alert("请输入正确的数字"):(localStorage.setItem("num",this.input),this.$router.push("/exercise"))}}},f={class:"learning"},v=a("div",{slot:"header",class:"clearfix"},[a("h1",null,"LEARNING")],-1);function N(y,e,V,b,l,i){const r=t("el-input"),u=t("el-button"),c=t("el-divider"),p=t("el-card");return _(),m("div",f,[n(p,{class:"box-card"},{default:s(()=>[v,n(r,{type:"text",placeholder:"请输入题目数量",modelValue:l.input,"onUpdate:modelValue":e[0]||(e[0]=o=>l.input=o),clearable:"",style:{width:"300px"}},null,8,["modelValue"]),n(u,{type:"primary",onClick:e[1]||(e[1]=o=>i.exer())},{default:s(()=>[h("开始测试")]),_:1}),n(c)]),_:1})])}const k=d(x,[["render",N]]);export{k as default};