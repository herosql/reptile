package com.weizhen.urltest;

import net.sf.json.JSONObject;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.HashMap;
import java.util.Map;

/**    //返回结果集进行map映射
 *   /*StringBuffer hql = new StringBuffer();
 *
 *         hql.append("select *,count(key_value) as amout,count(state =:state or null) as sums from wz_coupons where shops_id =:shops_id and state =:state group by key_value ");
 *
 *
 *         Query query = this.createNativeQuery(hql.toString(),map).setResultTransformer(Transformers.ALIAS_TO_ENTITY_MAP);
 *
 *         List result = query.list();
 *
 *         List<Coupons> coupons = BeanCopier.copyJSONList(result, Coupons.class);
 *
 *
 *         System.out.println(coupons.size());
 *
 *         return result;*/



/** hql语句将有关联的表进行关联查询,返回当前表的映射对象
 * String hql = " from wz_coupons where shops_id =:shops_id and state =:state group by key_value";
 *
 *        Query query = this.createQuery(hql,map);
 *
 *        List result = query.list();
 * */


/** 纯面对对象sql查询       无sql（缺点无法映射map(使用别名后可以),使用分组后(无法映射表的映射对象)）
 *  Criteria criteria = this.createCriteria();//Restrictions.eq("id", couponsRequest.getShopFansId().intValue())
 *
 *         criteria.add(Restrictions.eq("shops",iShopsDao.find((Integer) map.get("shops_id"))));
 *
 *          //下面两个写法不同，但效果一样，但字段需要与映射类中的元素字段一样
 *         criteria.add(Restrictions.eq("state",map.get("state")));
 *         //criteria.add(Property.forName("state").eq(map.get("state")));
 *
 *         ProjectionList projectionList = Projections.projectionList();
 *
 *         projectionList.add(Projections.groupProperty("key").as("keys"));
 *
 *         projectionList.add(Projections.count("key").as("sums"));
 *
 *         projectionList.add(Projections.property("shops").as("shops"));
 *
 *         criteria.setProjection(projectionList);
 *
 *         criteria.setResultTransformer(Transformers.ALIAS_TO_ENTITY_MAP);
 *
 *         return criteria.list();
 * */

public class UrlTest {


    public static void main(String arge[]) {
        Map<String, Object> map = new HashMap();
        /**
         * shopsid    店铺id
         * startTime  开始时间
         * endTime    结束时间
         * money      金额
         * amount     张数
         * astrict_money 满多少元使用
         * */
        /*map.put("astrict_money","100.00");
        map.put("openid","openid");
        map.put("startTime","2018-01-02");
        map.put("endTime","2018-01-06");
        map.put("money","20.00");
        map.put("amount","10");
        String send = "http://localhost:8080";
        send += "/coupons/create";*/

        /**
         *
         * openid    店铺 或 粉丝
         * state      优惠券状态
         * */
        /*map.put("openid","openid");
        map.put("state","2");
        String send = "http://localhost:8080";
        send += "/coupons/list";*/


        /**
         *   openid	    微信唯一标示
         *   state	    修改状态(1未领用，2已领用，3已使用，4失效)
         *   key_value  优惠券唯一标示
         *
         * */

        /**
         * 用户领取，使用优惠券
         * */

        /*map.put("openid","useropenid");
        map.put("key","48b4d439df58bde645a0962b");
        map.put("state","2");
        String send = "http://localhost:8080";
        send += "/coupons/update";*/

        /**
         * 商户删除优惠券
         * */
      /*  map.put("openid","openid");
        map.put("key_value","48b4d439df58bde645a0962b");
        map.put("state","4");
        String send = "http://localhost:8080";
        send += "/coupons/update";*/

      /**
       * 获取总计数
       * */
       /* map.put("openid","useropenid");
        String send = "http://localhost:8080";
        send += "/coupons/getCount";*/

       /**
        * 根据类别获取优惠券
        * */
       /* map.put("openid","useropenid");
        map.put("categoryId","1");
        String send = "http://localhost:8080";
        send += "/coupons/getCouponsQuery";*/

       /**
        * 获取轮播图
        * */
        /*map.put("get","get");
        String send = "http://localhost:8080";
        send += "/wx/system/getimg";*/

        /**
         * 获取粉丝福利
         * */
         /*map.put("openId","o40Yj0QokLu1tv-fd-VoMlw2PfTE");
        map.put("state","1");
        String send = "http://localhost:8080";
        send += "/order/getWelfare";*/

         /**
          * 获取粉丝
          *
          * */
       /* map.put("openid","o40Yj0QokLu1tv-fd-VoMlw2PfTEs");
        String send = "http://localhost:8080";
        send += "/wx/shops/getFans";*/

        /**
         *  创建优惠券(提交审核)
         *
         *  * astrictMoney    满多少元可进行使用
         *  * startTime       开始时间
         *  * endTime         结束时间
         *  * money            金额
         *  * amount           优惠券张数
         *
         * */
        map.put("astrictMoney","500");
        map.put("startTime","2018-01-02");
        map.put("endTime","2018-02-01");
        map.put("money","100");
        map.put("amount","100");

        String send = "http://localhost:8080";
        send += "/coupons/create";

        URL url = null;
        try {
            url = new URL(send);
            HttpURLConnection httpURLConnection = (HttpURLConnection) url.openConnection();
            httpURLConnection.setRequestMethod("POST");// 提交模式GET
            //httpURLConnection.setRequestMethod("GET");
            httpURLConnection.setConnectTimeout(10000);//连接超时 单位毫秒
            httpURLConnection.setReadTimeout(10000);//读取超时 单位毫秒
            // 发送POST请求必须设置如下两行
            httpURLConnection.setDoOutput(true);
            httpURLConnection.setDoInput(true);
            httpURLConnection.setRequestProperty("Charset", "UTF-8");
            httpURLConnection.setRequestProperty("Content-Type", "application/json");

            httpURLConnection.connect();
            OutputStream os = httpURLConnection.getOutputStream();
            os.write(JSONObject.fromObject(map).toString().getBytes("utf-8"));
            os.flush();

            StringBuilder sb = new StringBuilder();
            int httpRspCode = httpURLConnection.getResponseCode();
            if (httpRspCode == HttpURLConnection.HTTP_OK) {
                // 开始获取数据
                BufferedReader br = new BufferedReader(
                        new InputStreamReader(httpURLConnection.getInputStream(), "utf-8"));
                String line = null;
                while ((line = br.readLine()) != null) {
                    sb.append(line);
                }
                br.close();
                System.out.println(sb.toString());
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
