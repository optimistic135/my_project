import{a as _}from"./axios-21b846bc.js";import{_ as f,r as o,o as w,c as b,a as t,w as s,b as p,p as x,f as v,d as m}from"./index-49d31e09.js";const y={data(){return{alldata:[],data:""}},created(){this.getdata()},methods:{tableRowClassName({row:e,rowIndex:a}){return console.log(e.match),e.match==="×"?(console.log("nihao"),"red-row"):"success-row"},getdata(){const e=localStorage.getItem("responseData");_.post("/api/judge",JSON.parse(e)).then(a=>{console.log(a.data),this.alldata=a.data})},tolearning(){this.$confirm("此操作将返回学习界面, 是否继续?","提示",{confirmButtonText:"确定",cancelButtonText:"取消",type:"warning"}).then(()=>{localStorage.clear(),this.$router.push("/learning")}).catch(()=>{this.$message({type:"info",message:"已取消删除"})})},add(e){this.$confirm("此操作将添加单词进进词库, 是否继续?","提示",{confirmButtonText:"确定",cancelButtonText:"取消",type:"warning"}).then(()=>{const a={username:sessionStorage.getItem("username"),word:e.english,chinese:e.chinese};console.log(a),_.post("/api/addword",a).then(c=>{alert(c.data.message)})}).catch(()=>{this.$message({type:"info",message:"已取消"})})}}},B=e=>(x("data-v-e61f0033"),e=e(),v(),e),C={class:"result"},I=B(()=>m("div",{slot:"header",class:"clearfix"},[m("h3",null,"result")],-1));function S(e,a,c,$,u,l){const r=o("el-divider"),n=o("el-table-column"),d=o("el-button"),h=o("el-table"),g=o("el-card");return w(),b("div",C,[t(g,{class:"box-card"},{default:s(()=>[I,t(r),t(h,{data:u.alldata,style:{width:"100%"},"row-class-name":l.tableRowClassName},{default:s(()=>[t(n,{prop:"english",label:"单词",width:"250"}),t(n,{prop:"chinese",label:"中文",width:"250"}),t(n,{prop:"match",label:"结果",width:"250"}),t(n,{label:"操作"},{default:s(i=>[t(d,{type:"success",onClick:N=>l.add(i.row)},{default:s(()=>[p("添加到我的词库")]),_:2},1032,["onClick"])]),_:1})]),_:1},8,["data","row-class-name"]),t(r),t(d,{type:"primary",onClick:a[0]||(a[0]=i=>l.tolearning())},{default:s(()=>[p("返回学习界面")]),_:1})]),_:1})])}const V=f(y,[["render",S],["__scopeId","data-v-e61f0033"]]);export{V as default};
